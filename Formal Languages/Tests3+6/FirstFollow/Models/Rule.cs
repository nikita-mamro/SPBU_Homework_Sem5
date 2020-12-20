namespace FirstFollow.Models
{
    public class Rule
    {
        public string LeftSide { get; private set; }
        public string RightSide { get; private set; }

        public Rule(string left, string right)
        {
            LeftSide = left;
            RightSide = right;
        }
    }
}
