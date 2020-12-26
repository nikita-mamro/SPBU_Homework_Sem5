using FirstFollow.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace FirstFollow.Solver
{
    public class FirstFollowFinder
    {
        private readonly Grammar _g;

        public FirstFollowFinder(Grammar g)
        {
            _g = g;
        }

        public List<string> First(int k, string str)
        {
            var ntFirst = FirstForNonterminal(k);
            var strLists = new List<List<string>>();

            if (string.IsNullOrEmpty(str))
            {
                strLists.Add(new List<string> { "ε" });
            }

            foreach (var c in str)
            {
                if (char.IsUpper(c))
                {
                    strLists.Add(ntFirst[c]);
                }
                else
                {
                    strLists.Add(new List<string> { c.ToString() });
                }
            }

            var res = new List<string>();

            foreach (var l in strLists)
            {
                res = XorK(res, l, k);
            }

            return res;
        }

        public Dictionary<char, List<string>> FirstForNonterminal(int k)
        {
            // Создаём словарь для хранения списков F_i для каждого нетерминала
            // В List<List<string>> лежат последовательности F_i для нетерминала
            // В bool флаг, что F_j = F_j+1
            var fi = new Dictionary<char, (List<List<string>>, bool)>();
            foreach (var nt in _g.VN)
            {
                fi.Add(nt, (new List<List<string>>(), false));
            }

            // Построение F_0
            foreach (var nt in _g.VN)
            {
                // Добавляем F_0
                fi[nt].Item1.Add(new List<string>());

                foreach (var rule in _g.Rules)
                {
                    if (rule.LeftSide == nt.ToString())
                    {
                        // Берем за x цепочку терминалов в правой части правила до первого нетерминала
                        var x = rule.RightSide.TakeWhile(e => char.IsLower(e));

                        // Если |x| < k, проверяем, что α = ε
                        if (x.Count() < k)
                        {
                            var afterX = rule.RightSide.TakeLast(rule.RightSide.Length - x.Count());

                            if  (afterX.Count() != 0 && new string(afterX.ToArray()) != "ε")
                            {
                                continue;
                            }
                        }
                        // Если |x| > k, то меняем x на первые k терминалов из x
                        else if (x.Count() > k)
                        {
                            x = x.Take(k);
                        }

                        // Условия выполнены, добавляем x к F_0(nt)
                        fi[nt].Item1[0].Add(new string(x.ToArray()));
                    }
                }
            }

            var i = 0;

            // Построение остальных F_i (для i = 1,2,...), пока для всех нетерминалов
            // не получим F_j = F_j+1 для некоторого j
            while (fi.Values.Select(e => e.Item2).Contains(false))
            {
                foreach (var nt in _g.VN)
                {
                    var xs = new List<string>();

                    var yss = new List<string>();

                    foreach (var rule in _g.Rules)
                    {
                        // Проверка на правила вида A -> Y1...Ym
                        if (rule.LeftSide == nt.ToString() && !rule.RightSide.Any(e => !char.IsUpper(e)))
                        {
                            yss.Add(rule.RightSide);
                        }
                    }

                    foreach (var ys in yss)
                    {
                        var tmpRes = new List<string>();

                        foreach (var y in ys)
                        {
                            // ( Применяем ⊕k к F_j-1 (в данном случае это F_i) )
                            tmpRes = XorK(tmpRes, fi[y].Item1[i], k);
                        }

                        xs = tmpRes.Union(xs).Distinct().ToList();
                    }

                    var fj = fi[nt].Item1.Last();
                    var fj1 = fj.Union(xs).Distinct().ToList();
                    // Добавляем F_j+1
                    fi[nt].Item1.Add(fj1);

                    // Проверка на совпадение F_j(nt) и F_j+1(nt)
                    if (fj.SequenceEqual(fj1))
                    {
                        fi[nt] = (fi[nt].Item1, true);
                    }
                }

                ++i;
            }

            // Получение результата (набор FIRSTk для нетерминалов)
            var res = new Dictionary<char, List<string>>();

            foreach (var nt in _g.VN)
            {
                // Для каждого нетерминала
                // берём последний элемент списка F_i-ых
                res.Add(nt, fi[nt].Item1.Last());
            }

            return res;
        }

        /// <summary>
        /// Функция FOLLOW для нетерминалов
        /// </summary>
        public Dictionary<char, List<string>> FollowForNonterminal(int k)
        {
            var res = new Dictionary<char, List<string>>();

            var phis = GetPhis(k);

            foreach (var nt in _g.VN)
            {
                var follow = phis[('S', nt)].Where(e => e != "ε").ToList();

                if (nt == 'S')
                {
                    follow = follow.Union(new List<string> { "ε" }).ToList();
                }

                res.Add(nt, follow);
            }

            return res;
        }

        private Dictionary<(char, char), List<string>> GetPhis(int k)
        {
            var phis = new Dictionary<(char, char), List<List<string>>>();

            // Ищем ϕ_0
            foreach (var a in _g.VN)
            {
                foreach (var b in _g.VN)
                {
                    // Добавляем новую последовательность phi с пустым phi0
                    phis.Add((a, b), new List<List<string>>());
                    phis[(a, b)].Add(new List<string>());

                    foreach (var rule in _g.Rules)
                    {
                        // Ищем подходящие для phi0(a,b) w
                        if (rule.LeftSide == a.ToString())
                        {
                            foreach (var alpha in GetRightPartsForPhi0(rule.RightSide, b))
                            {
                                foreach (var w in First(k, alpha))
                                {
                                    phis[(a, b)][0].Add(w);
                                }
                            }
                        }
                    }
                }
            }

            // Нашли ϕ_0, ищем ϕ_1, ϕ_2,...

            var i = 0;
            bool finished;

            while (true)
            {
                finished = true;

                // Найдены ϕ_0,...,ϕ_i-1
                // Ищем ϕ_i+1
                foreach (var a in _g.VN)
                {
                    foreach (var b in _g.VN)
                    {
                        // Для ϕ_i+1
                        var phi_i1 = phis[(a, b)][i];

                        foreach (var rule in _g.Rules)
                        {
                            if (rule.LeftSide == a.ToString())
                            {
                                // Проверка, есть ли нетерминал Xp в правой части правила
                                if (rule.RightSide.Any(e => char.IsUpper(e)))
                                {
                                    // Для каждого нетерминала Xp выполняется шаг 2
                                    foreach (var nt in rule.RightSide.Where(e => char.IsUpper(e)))
                                    {
                                        var p = rule.RightSide.IndexOf(nt);
                                        // X_p+1...X_m
                                        var xs = rule.RightSide.Substring(p + 1, rule.RightSide.Length - p - 1);
                                        var ws = phis[(nt, b)][i];
                                        ws = XorK(ws, First(k, xs), k);

                                        phi_i1 = phi_i1.Union(ws).ToList();
                                    }
                                }
                            }
                        }

                        // Добавляем ϕ_i+1 к результатам
                        phis[(a, b)].Add(phi_i1);
                    }
                }

                foreach (var a in _g.VN)
                {
                    foreach (var b in _g.VN)
                    {
                        if (!phis[(a, b)][i].SequenceEqual(phis[(a, b)][i + 1]))
                        {
                            finished = false;
                        }
                    }
                }

                ++i;

                if (finished)
                {
                    break;
                }
            }

            var res = new Dictionary<(char, char), List<string>>();

            foreach (var a in _g.VN)
            {
                foreach (var b in _g.VN)
                {
                    res.Add((a, b), phis[(a, b)].Last());
                }
            }

            return res;
        }

        public List<string> XorK(List<string> l1, List<string> l2, int k)
        {
            var res = new List<string>();

            if (l1.Count == 0)
            {
                res = l2;
            }
            else if (l2.Count == 0)
            {
                res = l1;
            }
            else
            {
                foreach (var e1 in l1)
                {
                    foreach (var e2 in l2)
                    {
                        var toAdd = (e1 + e2).Replace("ε", string.Empty);

                        if (string.IsNullOrEmpty(toAdd))
                        {
                            toAdd = "ε";
                        }

                        res.Add(toAdd);
                    }
                }
            }

            return res.Select(e => new string(e.Take(k).ToArray())).Distinct().ToList();
        }

        private List<string> GetRightPartsForPhi0(string ruleRightSide, char b)
        {
            var res = new List<string>();

            for (var i = 0; i < ruleRightSide.Length; ++i)
            {
                if (ruleRightSide[i] == b)
                {
                    res.Add(ruleRightSide.Substring(i + 1, ruleRightSide.Length - i - 1));
                }
            }

            return res;
        }
    }
}
