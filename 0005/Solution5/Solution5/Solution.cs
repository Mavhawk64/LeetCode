using System;

namespace Solution5
{
    class Solution
    {
        static void Main(string[] args)
        {
            Console.WriteLine(LongestPalindrome("mom"));
        }

        public static string LongestPalindrome(string s)
        {
            // Monacher's Algorithm
            var sp = "#";
            foreach (var item in s)
            {
                sp += item + "#";
            }
            var pr = new int[2 * s.Length + 1];

            var c = 0;
            var r = 0;


            while (c < sp.Length)
            {
                while (c - (r + 1) >= 0 && c + (r + 1) < sp.Length && sp[c - (r + 1)] == sp[c + (r + 1)])
                {
                    r++;
                }

                pr[c] = r;

                var oc = c;
                var or = r;
                c++;
                r = 0;
                while (c <= oc + or)
                {
                    var mc = oc - (c - oc);
                    var mmr = oc + or - c;
                    if (pr[mc] < mmr)
                    {
                        pr[c] = pr[mc];
                        c++;
                    }
                    else if (pr[mc] > mmr)
                    {
                        pr[c] = mmr;
                        c++;
                    }
                    else
                    {
                        r = mmr;
                        break;
                    }
                }
            }
            var t = get_max(pr);
            var y = get_max_index(pr);
            var temp = sp.Substring(y-t,y+t+1);
            var longest_palindrome_in_S = "";
            foreach (var item in temp)
            {
                if(item != '#')
                {
                    longest_palindrome_in_S += item;
                }
            }
            return longest_palindrome_in_S;
        }

        private static int get_max_index(int[] pr)
        {
            int max = 0;
            int index = 0;
            for(int i = 0; i < pr.Length; i++)
            {
                var item = pr[i];
                if (item > max)
                {
                    max = item;
                    index = i;
                }
            }
            return index;
        }

        private static int get_max(int[] pr)
        {
            int max = 0;
            foreach (var item in pr)
            {
                if (item > max)
                    max = item;
            }
            return max;
        }
    }
}
