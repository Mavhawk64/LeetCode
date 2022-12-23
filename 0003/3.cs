// Accepted: 08/05/2021
public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if (s.Length == 0) return 0;
            bool isOneChar = true;
            for (int i = 1; i < s.Length; i++)
            {
                isOneChar = isOneChar && s[i] == s[i - 1];
            }
            if (isOneChar) return 1;
            string longest = "";
            string builder = "";
            int start = 0;

            for (int i = 0; i < s.Length; i++)
            {
                char c = s[i];
                if (!builder.Contains(c))
                {
                    builder += c;
                }
                else
                {
                    i = s.IndexOf(s.Substring(start, s.Length - start)) + builder.IndexOf(c);
                    if (longest.Length < builder.Length) longest = builder;
                    builder = "";
                    if (i + 1 > start)
                        start = i;
                    start++;
                }
                if (longest.Length < builder.Length) longest = builder;
                if (s.Length - start <= longest.Length) break;
            }
            return longest.Length;
    }
}