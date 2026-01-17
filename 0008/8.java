// Accepted: 01/17/2026

class Solution {

    public int myAtoi(String s) {
        s = s.trim();
        int ret = 0;
        byte sign = 1;
        if (s.isEmpty()) {
            return 0;
        }
        int index = 0;
        if (s.charAt(index) == '+' || s.charAt(index) == '-') {
            if (s.charAt(index) == '-') {
                sign = -1;
            }
            index++;
        }
        // remaining *should* be digits
        for (; index < s.length(); ++index) {
            char c = s.charAt(index);
            if (c < '0' || c > '9') {
                break;
            }
            int digit = c - '0';
            // Check for overflow/underflow
            if (ret > (Integer.MAX_VALUE - digit) / 10) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            ret = ret * 10 + digit;
        }

        return sign * ret;
    }
}

@SuppressWarnings("unused")
class Test {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.myAtoi("42")); // 42
        System.out.println(s.myAtoi("   -042")); // -42
        System.out.println(s.myAtoi("1337c0d3")); // 1337
        System.out.println(s.myAtoi("0-1")); // 0
        System.out.println(s.myAtoi("words and 987")); // 0
    }
}
