using FirstFollow.Models;
using System;
using System.Collections.Generic;

namespace FirstFollow.Utils
{
    public static class GrammarReader
    {
        public static Grammar ReadGrammar()
        {
            var rules = new List<Rule>();
            var vt = new List<char>();
            var vn = new List<char>();

            Console.WriteLine("Введите построчно правила в формате 'left->right':");

            var ruleInput = Console.ReadLine();

            while (!string.IsNullOrEmpty(ruleInput))
            {
                rules.Add(ParseRuleInput(ruleInput));
                ruleInput = Console.ReadLine();
            }

            foreach (var rule in rules)
            {
                foreach (var leftC in rule.LeftSide)
                {
                    if (Char.IsUpper(leftC))
                    {
                        if (!vn.Contains(leftC))
                        {
                            vn.Add(leftC);
                        }
                    }
                    else
                    {
                        if (!vt.Contains(leftC))
                        {
                            vt.Add(leftC);
                        }
                    }
                }

                foreach (var rightC in rule.RightSide)
                {
                    if (Char.IsUpper(rightC))
                    {
                        if (!vn.Contains(rightC))
                        {
                            vn.Add(rightC);
                        }
                    }
                    else
                    {
                        if (!vt.Contains(rightC))
                        {
                            vt.Add(rightC);
                        }
                    }
                }
            }

            if (!vn.Contains('S'))
            {
                throw new FormatException("Не обнаружен начальный нетерминал S");
            }

            return new Grammar(vt, vn, rules);
        }

        private static Rule ParseRuleInput(string input)
        {
            input = input.Replace(" ", string.Empty);
            var parts = input.Split("->");

            if (parts.Length != 2)
            {
                throw new FormatException("Неверный формат правила");
            }

            return new Rule(parts[0], parts[1]);
        }
    }
}
