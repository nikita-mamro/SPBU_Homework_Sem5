using FirstFollow.Models;
using FirstFollow.Solver;
using FirstFollow.Utils;
using System;
using System.Linq;

namespace FirstFollow
{
    public class Program
    {
        public static void Main()
        {
            Grammar grammar;

            while (true)
            {
                try
                {
                    grammar = GrammarReader.ReadGrammar();
                    break;
                }
                catch
                {
                    Console.WriteLine("Неверный формат ввода");
                }
            }

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

            var solver = new FirstFollowFinder(grammar);

            int k;
            while (true)
            {
                Console.Write("Введите k: ");
                var res = int.TryParse(Console.ReadLine(), out k);
                if (res && k > 0)
                {
                    break;
                }
            }

            Console.WriteLine("\nFIRSTk для нетерминалов:");
            var firsts = solver.FirstForNonterminal(k);
            foreach (var nt in firsts.Keys)
            {
                Console.Write($"FIRST({nt}): {{ ");
                foreach (var e in firsts[nt])
                {
                    Console.Write($"{e}");

                    if (firsts[nt].IndexOf(e) != firsts[nt].Count - 1)
                    {
                        Console.Write($",");
                    }

                    Console.Write(" ");
                }
                Console.WriteLine("}");
            }

            Console.WriteLine("\nFOLLOWk для нетерминалов:");
            var follows = solver.FollowForNonterminal(k);
            foreach (var nt in follows.Keys)
            {
                Console.Write($"FOLLOW({nt}): {{ ");
                foreach (var e in follows[nt])
                {
                    Console.Write($"{e}");

                    if (follows[nt].IndexOf(e) != follows[nt].Count - 1)
                    {
                        Console.Write($",");
                    }

                    Console.Write(" ");
                }
                Console.WriteLine("}");
            }
        }
    }
}
