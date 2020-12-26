using FirstFollow.Models;
using FirstFollow.Solver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CourseWork
{
    public static class LLkTester
    {
        private static List<List<string>> Sigma(char nt, Grammar g, FirstFollowFinder firstFollowFinder)
        {
            return new List<List<string>>();
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
                    var ls = Sigma(nt, g, helper);
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
