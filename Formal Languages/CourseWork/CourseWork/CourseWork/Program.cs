using FirstFollow.Models;
using System;
using System.Collections.Generic;
using System.Linq;

namespace CourseWork
{
    public class Program
    {
        public static void Main(string[] args)
        {
            #region Grammar descriptions

            var vt1 = new List<char> { 'a', 'b' };

            var vn1 = new List<char> { 'S', 'B', 'A' };

            var rules1 = new List<Rule>
            {
                new Rule("S", "aB"),
                new Rule("S", "bA"),
                new Rule("A", "a"),
                new Rule("B", "b"),
                new Rule("A", "bAA"),
                new Rule("B", "aBB"),
                new Rule("A", "aS"),
                new Rule("B", "bS")
            };

            #endregion

            var vt = vt1;
            var vn = vn1;
            var rules = rules1;

            var grammar = new Grammar(vt, vn, rules);

            Console.WriteLine("Грамматика G:");
            Console.Write("\nVn: { ");
            for (var i = 0; i < grammar.VN.Count - 1; ++i)
            {
                Console.Write($"{grammar.VN[i]}, ");
            }
            Console.Write($"{grammar.VN.Last()} }}");
            Console.Write("\nVt: { ");
            for (var i = 0; i < grammar.VT.Count - 1; ++i)
            {
                Console.Write($"{grammar.VT[i]}, ");
            }
            Console.Write($"{grammar.VT.Last()} }}");
            Console.WriteLine("\nПравила: ");
            foreach (var rule in grammar.Rules)
            {
                Console.WriteLine($"{rule.LeftSide} -> {rule.RightSide}");
            }

            //int k;
            //while (true)
            //{
            //    Console.Write("Введите натуральное k: ");
            //    var res = int.TryParse(Console.ReadLine(), out k);
            //    if (res && k > 0)
            //    {
            //        break;
            //    }
            //}

            var k = 1;

            Console.WriteLine($"Грамматика G{(LLkTester.IsLLk(grammar, k) ? " " : " не ")}принадлежит классу LL({k})");

            k = 2;

            Console.WriteLine($"Грамматика G{(LLkTester.IsLLk(grammar, k) ? " " : " не ")}принадлежит классу LL({k})");

            k = 3;

            Console.WriteLine($"Грамматика G{(LLkTester.IsLLk(grammar, k) ? " " : " не ")}принадлежит классу LL({k})");

        }
    }
}
