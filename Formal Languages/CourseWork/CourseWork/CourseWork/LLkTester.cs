using FirstFollow.Models;
using FirstFollow.Solver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace CourseWork
{
    public static class LLkTester
    {
        private static List<string> FindLMResults(string str, Grammar g)
        {
            var res = new List<string>();

            if (str.Any(e => char.IsUpper(e)))
            {
                var leftNt = str.First(e => char.IsUpper(e));
                var regex = new Regex(Regex.Escape(leftNt.ToString()));
                var rules = g.Rules.Where(e => e.LeftSide == leftNt.ToString());

                foreach (var rule in rules)
                {
                    res.Add(regex.Replace(str, rule.RightSide, 1));
                }
            }

            return res;
        }

        private static Dictionary<(char, char), List<List<string>>> SigmaI(Grammar g, FirstFollowFinder firstFollowFinder, int k)
        {
            // Строим sigma_0
            var sigma_0 = new Dictionary<(char, char), List<List<string>>>();

            foreach (var ntA in g.VN)
            {
                foreach (var ntB in g.VN)
                {
                    sigma_0.Add((ntA, ntB), new List<List<string>>());
                    sigma_0[(ntA, ntB)].Add(new List<string>());

                    foreach (var rule in g.Rules)
                    {
                        if (rule.LeftSide == ntA.ToString())
                        {
                            if (rule.RightSide.Contains(ntB))
                            {
                                for (var i = 0; i < rule.RightSide.Length; ++i)
                                {
                                    if (rule.RightSide[i] == ntB)
                                    {
                                        var alpha = rule.RightSide.Substring(i + 1, rule.RightSide.Length - i - 1);
                                        sigma_0[(ntA, ntB)].Add(firstFollowFinder.First(k, alpha));
                                    }
                                }
                            }
                        }
                    }
                }
            }

            // Нашли sigma_0
            // Строим 1, 2, ...
            var sigma_1 = new Dictionary<(char, char), List<List<string>>>();
            var finished = false;

            while (!finished)
            {
                sigma_1 = new Dictionary<(char, char), List<List<string>>>();

                foreach (var ntA in g.VN)
                {
                    foreach (var ntB in g.VN)
                    {
                        sigma_1.Add((ntA, ntB), new List<List<string>>());
                        sigma_1[(ntA, ntB)].Add(new List<string>());

                        foreach (var rule in g.Rules)
                        {
                            for (var i = 0; i < rule.RightSide.Length; ++i)
                            {
                                if (char.IsUpper(rule.RightSide[i]))
                                {
                                    foreach (var lI in sigma_0[(rule.RightSide[i], ntB)])
                                    {
                                        var xs = rule.RightSide.Substring(i + 1, rule.RightSide.Length - i - 1);
                                        var first = firstFollowFinder.First(k, xs);
                                        var l = firstFollowFinder.XorK(lI, first, k);
                                        sigma_1[(ntA, ntB)].Add(l);
                                    }
                                }
                            }
                        }

                        sigma_1[(ntA, ntB)] = sigma_0[(ntA, ntB)].Union(sigma_1[(ntA, ntB)]).ToList();
                    }
                }

                finished = true;

                foreach (var ntA in g.VN)
                {
                    foreach (var ntB in g.VN)
                    {
                        var current = sigma_1[(ntA, ntB)];
                        var prev = sigma_0[(ntA, ntB)];

                        foreach (var l in current)
                        {
                            if (!prev.Any(e => e.SequenceEqual(l)))
                            {
                                finished = true;
                            }
                        }

                        foreach (var l in prev)
                        {
                            if (!current.Any(e => e.SequenceEqual(l)))
                            {
                                finished = true;
                            }
                        }
                    }
                }

                sigma_0 = sigma_1;
            }

            return sigma_1;
        }

        private static List<List<string>> Sigma(char nt, Grammar g, FirstFollowFinder firstFollowFinder, int k)
        {
            var sigmaI = SigmaI(g, firstFollowFinder, k);

            var res = sigmaI[('S', nt)];

            if (nt == 'S')
            {
                res = res.Union(new List<List<string>> { new List<string> { "ε" } }).ToList();
            }

            return res;
        }

        private static bool TwoOreMoreAlternativesExist(Grammar g, char nt)
        {
            return
                g.Rules
                .Select(e => e.LeftSide)
                .Where(e => e == nt.ToString())
                .Count() >= 2;
        }

        private static List<(Rule, Rule)> GetRulesPairs(Grammar g, char nt)
        {
            var ntRules = g.Rules.Where(e => e.LeftSide == nt.ToString());

            var res = new List<(Rule, Rule)>();

            foreach (var ruleA in ntRules)
            {
                foreach (var ruleB in ntRules)
                {
                    if (ruleA.RightSide != ruleB.RightSide)
                    {
                        if (!res.Any(e => e.Item1.RightSide == ruleA.RightSide && e.Item2.RightSide == ruleB.RightSide || e.Item1.RightSide == ruleB.RightSide && e.Item2.RightSide == ruleA.RightSide))
                        {
                            res.Add((ruleA, ruleB));
                        }
                    }
                }
            }

            return res;
        }

        public static bool IsLLk(Grammar g, int k)
        {
            var helper = new FirstFollowFinder(g);

            foreach (var nt in g.VN)
            {
                if (TwoOreMoreAlternativesExist(g, nt))
                {
                    var ls = Sigma(nt, g, helper, k);
                    var rulePairs = GetRulesPairs(g, nt);

                    foreach (var rulePair in rulePairs)
                    {
                        var beta = rulePair.Item1.RightSide;
                        var gamma = rulePair.Item2.RightSide;

                        foreach (var l in ls)
                        {
                            var fl = (helper.XorK(helper.First(k, beta), l, k)).Intersect(helper.XorK(helper.First(k, gamma), l, k));

                            if (fl.Any())
                            {
                                return false;
                            }
                        }
                    }
                }
            }

            return true;
        }
    }
}
