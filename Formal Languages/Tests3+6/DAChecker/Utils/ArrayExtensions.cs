using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DAWorker.Utils
{
    public static class ArrayExtensions
    {
        public static T[] GetColumn<T>(this T[,] matrix, int columnNumber)
        {
            return Enumerable.Range(0, matrix.GetLength(0))
                    .Select(x => matrix[x, columnNumber])
                    .ToArray();
        }

        public static T[] GetRow<T>(this T[,] matrix, int rowNumber)
        {
            return Enumerable.Range(0, matrix.GetLength(1))
                    .Select(x => matrix[rowNumber, x])
                    .ToArray();
        }

        public static void PrintPretty<T>(this T[,] matrix)
        {
            for (int i = 0; i < matrix.GetColumn(0).Length; i++)
            {
                for (int j = 0; j < matrix.GetRow(0).Length; j++)
                {
                    Console.Write(string.Format("{0} ", matrix[i, j] != null ? matrix[i, j].ToString() : "-"));
                }
                Console.Write(Environment.NewLine + Environment.NewLine);
            }
        }
    }
}
