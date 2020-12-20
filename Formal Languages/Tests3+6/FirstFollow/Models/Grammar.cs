using System.Collections.Generic;

namespace FirstFollow.Models
{
    public class Grammar
    {
        public List<char> VT { get; private set; }
        public List<char> VN { get; private set; }
        public List<Rule> Rules { get; private set; }

        public Grammar(List<char> vt, List<char> vn, List<Rule> rules)
        {
            VT = vt;
            VN = vn;
            Rules = rules;
        }
    }
}
