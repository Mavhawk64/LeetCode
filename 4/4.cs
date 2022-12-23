// Accepted: 08/09/2021
public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums = new int[nums1.Length + nums2.Length];
            int i = 0;
            int j = 0;
            for (int k = 0; k < nums.Length; k++)
            {
                if (i == nums1.Length)
                {
                    for (; j < nums2.Length; j++)
                    {
                        nums[k++] = nums2[j];
                    }
                    break;
                }
                else if (j == nums2.Length)
                {
                    for (; i < nums1.Length; i++)
                    {
                        nums[k++] = nums1[i];
                    }
                    break;
                } else
                {
                    if(nums1[i] < nums2[j])
                    {
                        nums[k] = nums1[i++];
                    } else
                    {
                        nums[k] = nums2[j++];
                    }
                }
                //Console.WriteLine(nums[k].ToString());
            }

            if (nums.Length % 2 == 0)
            {
                return (double)(nums[nums.Length / 2 - 1] + nums[nums.Length / 2]) / 2.0;
            }
            return nums[nums.Length / 2];

        }
}