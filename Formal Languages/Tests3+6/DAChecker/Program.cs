using DAWorker.Minimizer;
using DAWorker.Utils;
using System;
using System.Linq;

namespace DAWorker
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var entryAlphabet = new char[] { 'd', '.', 'e', '±', 'ε' };
            // Представление матрицы переходов
            // qi : i (i >= 0, q0 --- начальное состояние)
            // # : -1
            // пустая клетка: null
            var table = new int?[,]
            {
                { 1, null, null, null, null, null },
                { 1, 2, 3, null, null, -1 },
                { 4, null, null, null, null, null },
                { 5, null, null, null, 6, null },
                { 4, null, null, 3, null, -1 },
                { 5, null, null, null, null, -1 },
                { 5, null, null, null, null, null },
            };

            var minimizer = new DAMinimizer();
            minimizer.MinimizeDA(table, entryAlphabet);
        }
    }
}
