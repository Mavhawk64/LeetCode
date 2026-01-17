// Accepted: 01/17/2026
Console.WriteLine("LeetCode 9");
var solution = new Solution();

public class Solution
{
    public bool IsPalindrome(int x)
    {
        if (x < 0) return false;

        string s = x.ToString();
        int i = 0, j = s.Length - 1;

        while (i < j)
        {
            if (s[i] != s[j]) return false;
            i++;
            j--;
        }

        return true;
    }
}


// fn is_palindrome(x: String) -> bool {
//     let mut c: Vec<char> = x.chars().collect();
//     while !c.is_empty() {
//         if c.len() == 1 {
//             break;
//         }
//         let f: char = c.remove(0);
//         let e: Option<char> = c.pop();
//         if Some(f) != e {
//             return false;
//         }
//     }
//     true
// }
