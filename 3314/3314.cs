// Accepted: 01/19/2026
public class Solution
{
    public int[] MinBitwiseArray(IList<int> nums)
    {
        Dictionary<int, int> map = new Dictionary<int, int>();
        // since 2 <= nums[i] <= 1000, we can use a fixed size array for counting
        for(int i = 0; i <= 1000; ++i) {
            map[i | (i + 1)] = Math.Min(map.GetValueOrDefault(i | (i + 1), int.MaxValue), i);
        }
        int[] ans = new int[nums.Count];
        for(int i = 0; i < nums.Count; ++i) {
            ans[i] = map.GetValueOrDefault(nums[i], -1);
        }
        return ans;
    }
}
