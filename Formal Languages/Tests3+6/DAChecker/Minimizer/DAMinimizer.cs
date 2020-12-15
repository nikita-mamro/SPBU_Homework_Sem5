using DAWorker.Utils;
using DAWorker.Utils.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DAWorker.Minimizer
{
    public class DAMinimizer
    {
        private class DAHelper
        {
            private List<int> reachable;
            private List<Pair> pairs;
            private readonly int?[,] _table;
            private int?[,] minimizedTable;
            private readonly char[] _entryAlphabet;
            private int[] equivalenceClasses;

            public DAHelper(int?[,] table, char[] entryAlphabet)
            {
                _table = table;
                _entryAlphabet = entryAlphabet;
                equivalenceClasses = Enumerable.Range(0, table.GetColumn(0).Length).ToArray();
            }

            /// <summary>
            /// Поиск достижимых из начального состояний по таблице
            /// </summary>
            private void setReachableFromStart()
            {
                var visited = new bool[_table.Length];
                var q = new Queue<int>();
                q.Enqueue(0);
                visited[0] = true;

                var res = new List<int> { 0 };

                while (q.Count != 0)
                {
                    var current = q.Dequeue();

                    foreach (var neighbour in _table.GetRow(current))
                    {
                        if (neighbour.HasValue && (neighbour.Value == -1 || !visited[neighbour.Value]))
                        {
                            if (neighbour.Value == -1)
                            {
                                if (!res.Contains(-1))
                                {
                                    res.Add(-1);
                                }

                                continue;
                            }

                            q.Enqueue(neighbour.Value);
                            visited[neighbour.Value] = true;
                            res.Add(neighbour.Value);
                        }
                    }
                }

                reachable = res;
            }

            /// <summary>
            /// Генерация всевозможных пар состояний
            /// </summary>
            private void setPossibleStatePairs()
            {
                pairs = new List<Pair>();

                foreach (var state1 in reachable)
                {
                    foreach (var state2 in reachable)
                    {
                        var existingPair = pairs.SingleOrDefault(e => e.P == state1 && e.Q == state2 || e.P == state2 && e.Q == state1);

                        if (existingPair == null)
                        {
                            pairs.Add(new Pair(Math.Min(state1, state2), Math.Max(state1, state2)));
                        }
                    }
                }
            }

            /// <summary>
            /// Разметка пар
            /// </summary>
            private void markPairs()
            {
                // Отмечаются пары, где одно состояние конечное, другое --- нет
                foreach (var pair in pairs)
                {
                    if (pair.P == -1 || pair.Q == -1)
                    {
                        pair.Marked = true;
                    }
                }

                // Отмечаются пары (p, q) такие, что для некоторого a отмечена пара (δ(p,a),δ(q,a))
                bool beingChanged;

                do
                {
                    beingChanged = false;

                    foreach (var pair in pairs)
                    {
                        if (!pair.Marked)
                        {
                            // Идём по всем входным символам, для наглядности назовём счётчик a вместо привычных i/j
                            for (var a = 0; a < _table.GetRow(0).Length; ++a)
                            {
                                // Для каждого входного символа проверяем, отмечена ли пара (δ(p,a),δ(q,a)) (или (δ(q,a),δ(p,a)))
                                var dpa = _table[pair.P, a]; // δ(p,a)
                                var dqa = _table[pair.Q, a]; // δ(q,a)

                                if (dpa != null && dqa != null)
                                {
                                    // Ищем пару (δ(p,a),δ(q,a)) или (δ(q,a),δ(p,a))
                                    var existingPair = pairs.SingleOrDefault(e => e.P == dpa && e.Q == dqa || e.P == dqa && e.Q == dpa);

                                    // Если такая есть и она отмечена, отмечаем текущую
                                    if (pair != null && pair.Marked)
                                    {
                                        pair.Marked = true;
                                        beingChanged = true;
                                        goto exit;
                                    }
                                }
                            }
                        }
                    }
                exit:;
                }
                while (beingChanged);
            }

            /// <summary>
            /// Все необходимые действия с множеством пар
            /// </summary>
            private void preparePairs()
            {
                // Шаг 1: отделяем достижимые состояния
                setReachableFromStart();
                // Шаг 2: создаем набор всевозможных пар состояний
                setPossibleStatePairs();
                // Шаг 3: помечаем пары, где ровно одно состояние конечное,
                // либо такие, что помечена (δ(p,a),δ(q,a)) для некоторого
                // a из входного алфавита
                // В итоге у нас получится, что отмеченными будут пары эквивалентных состояний
                markPairs();
            }

            /// <summary>
            /// Установка корректных значений в массив с информацией о классах эквивалентности
            /// </summary>
            private void setEquivalenceClasses()
            {
                // Идём по всем отмеченным парам эквивалентных состояний
                foreach (var pair in pairs.Where(e => e.Marked))
                {
                    // Идём по всем состояниям
                    for (var state = 0; state < _table.GetColumn(0).Length; ++state)
                    {
                        // Пара (p, q) отмечена => p и q эквивалентны
                        // Например, если эквивалентны состояния 1 и 2,
                        // в equivalenceClasses будет так: ...[1] = 2, ...[2] = 2
                        // Таким образом в i-ой ячейке лежит значение 1 элемента из класса эквивалентности, в котором находится i
                        if (equivalenceClasses[state] == pair.P)
                        {
                            equivalenceClasses[state] = pair.Q;
                        }
                    }
                }
            }

            /// <summary>
            /// Генерация минимизированного автомата
            /// </summary>
            public int?[,] GenerateMinimizedDA()
            {
                // Создаём и проводим разметку пар
                preparePairs();
                var isMinimized = !pairs.Any(e => e.P != -1 && e.Q != -1 && e.Marked);

                // Нет отмеченных пар => был дан минимальный автомат
                if (isMinimized)
                {
                    Console.WriteLine("Автомат уже был минимален по кол-ву состояний");
                    minimizedTable = _table;
                }
                else
                {
                    // Подготавливаем эквивалентные состояния
                    setEquivalenceClasses();

                    // Количество классов эквивалентности
                    var statesNumber = equivalenceClasses.Distinct().Count();

                    var res = new List<List<int?>>();

                    for (var i = 0; i < _table.Length; ++i)
                    {
                        res.Add(_table.GetRow(i).ToList());
                    }

                    foreach (var row in res)
                    {
                        for (var i = 0; i < row.Count; ++i)
                        {
                            if (row[i].HasValue && row[i] != -1)
                            {
                                row[i] = equivalenceClasses[row[i].Value];
                            }
                        }
                    }

                    var rowsToRemove = equivalenceClasses.Where(e => e != equivalenceClasses.ToList().IndexOf(e));

                    var minimized = new List<List<int?>>();

                    for (var i = 0; i < res.Count; ++i)
                    {
                        if (!rowsToRemove.Contains(i))
                        {
                            minimized.Add(res[i]);
                        }
                    }

                    minimizedTable = new int?[minimized.Count, minimized[0].Count];

                    for (var row = 0; row < minimized.Count; ++row)
                    {
                        for (var col = 0; col < minimized[0].Count; ++col)
                        {
                            minimizedTable[row, col] = minimized[row][col];
                        }
                    }
                }

                minimizedTable.PrintPretty();

                return minimizedTable;
            }
        }

        public int?[,] MinimizeDA(int?[,] table, char[] entryAlphabet)
        {
            var helper = new DAHelper(table, entryAlphabet);
            return helper.GenerateMinimizedDA();
        }
    }
}
