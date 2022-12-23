// Accepted: 08/04/2021
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode c1 = l1;
            string ns1 = "";
            while (c1 != null)
            {
                ns1 = c1.val + ns1;
                c1 = c1.next;
            }
            ListNode c2 = l2;
            string ns2 = "";
            while (c2 != null)
            {
                ns2 = c2.val + ns2;
                c2 = c2.next;
            }
            string longer = ns1.Length > ns2.Length ? ns1 : ns2;
            string s = "";
            int rollOver = 0;
            for (int i = 0; i < longer.Length; i++)
            {
                int n1 = ns1.Length - i - 1;
                int n2 = ns2.Length - i - 1;
                int sum = rollOver;
                if (n1 >= 0)
                    sum += int.Parse(ns1.Substring(n1, 1));
                if (n2 >= 0)
                    sum += int.Parse(ns2.Substring(n2, 1));
                rollOver = 0;
                while (sum > 9)
                {
                    rollOver++;
                    sum -= 10;
                }
                s = sum + s;
            }
            while(rollOver > 9)
            {
                s = 9 + s;
                rollOver -= 9;
            }
            if(rollOver > 0)
            {
                s = rollOver + s;
            }
            ListNode r = null;
            while (!s.Equals(""))
            {
                r = new ListNode(int.Parse(s.Substring(0, 1)), r);
                s = s.Substring(1, s.Length - 1);
            }
            return r;
        }
}