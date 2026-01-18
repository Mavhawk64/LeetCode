
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

class Solution {

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int cmp = nums[i] + nums[left] + nums[right];
                if (cmp == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    // 1. Move pointers to avoid the current values
                    left++;
                    right--;

                    // 2. SKIP DUPLICATES: Keep moving if the next numbers are the same
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                } else if (cmp < 0) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        return res;
    }

    // O(n^2) solution using precomputation of two-sum combinations
    // TLE on large inputs
    public List<List<Integer>> bigO_n_squared_threeSum(int[] nums) {
        HashSet<List<Integer>> ret = new HashSet<>();
        Arrays.sort(nums);

        // Precompute all two-sum combinations
        HashMap<Integer, List<List<Integer>>> twoSum = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            for (int j = i + 1; j < nums.length; ++j) {
                int sum = nums[i] + nums[j];
                twoSum.putIfAbsent(sum, new ArrayList<>());
                twoSum.get(sum).add(Arrays.asList(i, j));
            }
        }

        // Find all three-sum combinations
        for (int i = 0; i < nums.length; ++i) {
            int target = -nums[i];
            if (twoSum.containsKey(target)) {
                for (List<Integer> pair : twoSum.get(target)) {
                    if (pair.get(0) != i && pair.get(1) != i) {
                        List<Integer> triplet = Arrays.asList(nums[i], nums[pair.get(0)], nums[pair.get(1)]);
                        Collections.sort(triplet);
                        ret.add(triplet);
                    }
                }
            }
        }

        // sort each triplet to ensure uniqueness
        HashSet<List<Integer>> sortedRet = new HashSet<>();
        for (List<Integer> triplet : ret) {
            List<Integer> sortedTriplet = new ArrayList<>(triplet);
            sortedTriplet.sort(Integer::compareTo);
            sortedRet.add(sortedTriplet);
        }
        return new ArrayList<>(sortedRet);
    }
}

// Example usage
class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        // [-1,0,1,2,-1,-4]
        // [0,1,1]
        // [0,0,0]
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = solution.threeSum(nums);
        for (List<Integer> triplet : result) {
            System.out.print(triplet);
            System.out.print(" ");
        }

        System.out.println();

        nums = new int[]{0, 1, 1};
        result = solution.threeSum(nums);
        for (List<Integer> triplet : result) {
            System.out.print(triplet);
            System.out.print(" ");
        }
        System.out.println();
        nums = new int[]{0, 0, 0};
        result = solution.threeSum(nums);
        for (List<Integer> triplet : result) {
            System.out.print(triplet);
            System.out.print(" ");
        }
        System.out.println();
        // [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
        // Expected: [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]
        nums = new int[]{2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10};
        result = solution.threeSum(nums);
        for (List<Integer> triplet : result) {
            System.out.print(triplet);
            System.out.print(" ");
        }
        System.out.println();
    }
}
