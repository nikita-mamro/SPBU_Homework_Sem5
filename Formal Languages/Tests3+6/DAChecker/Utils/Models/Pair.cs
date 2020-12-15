using System;
using System.Collections.Generic;
using System.Text;

namespace DAWorker.Utils.Models
{
    public class Pair
    {
        public int P { get; set; }
        public int Q { get; set; }
        public bool Marked { get; set; }

        public Pair(int p, int q)
        {
            P = p;
            Q = q;
        }
    }
}
