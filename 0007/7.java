// Accepted: 01/14/2026

class Solution {
  public int reverse(int x) {
    // Silly solution with try/catch... I tried to get it in one line :(
    try {
      return (x < 0 ? -1 : 1) * Integer.parseInt(new String(reverse(("" + Math.abs(x)).toCharArray())));
    } catch (NumberFormatException e) {
      return 0;
    }
  }

  private char[] reverse(char[] arr) {
    for (int i = 0; i < arr.length / 2; ++i) {
      char temp = arr[i];
      arr[i] = arr[arr.length - i - 1];
      arr[arr.length - i - 1] = temp;
    }
    return arr;
  }
}

// Here is my rust solution for reference
// reversed_num: u128 = num
// .to_string()
// .chars()
// .rev()
// .collect::<String>()
// .parse()
// .unwrap();

@SuppressWarnings("unused")
class Test {
  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.reverse(123));
    System.out.println(s.reverse(-123));
    System.out.println(s.reverse(123456789));
    System.out.println(s.reverse(Integer.MAX_VALUE)); // too big when backwards!
    // Biggest palindrome:
    System.out.println(s.reverse(2147447412));
  }
}
