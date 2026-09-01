// Accepted: 08/30/2026

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;

class Solution {

    private int sumArr(int[] arr) {
        int s = 0;
        for (int i = 0; i < arr.length; ++i) {
            s += arr[i];
        }
        return s;
    }

    private int[] splitArrAndTrash(int[] arr) {
        int[] left = Arrays.copyOfRange(arr, 0, arr.length / 2);
        int[] right = Arrays.copyOfRange(arr, arr.length / 2, arr.length);

        System.out.println(Arrays.toString(left) + " <> " + Arrays.toString(right));

        if (sumArr(left) > sumArr(right)) {
            return right;
        }
        return left;
    }

    private int[] getPrefixSum(int[] arr) {
        int[] prefix = new int[arr.length + 1];
        for (int i = 1; i <= arr.length; ++i) {
            prefix[i] = prefix[i - 1] + arr[i - 1];
        }
        return prefix;
    }

    private int getBestSplitSums(int leftIdx, int rightIdx, int[][] memo, int[] prefix, int _debugDepth) {
        // System.out.println("[DEBUG] depth = " + _debugDepth);

        if (leftIdx >= rightIdx) {
            return 0;
        }

        if (memo[leftIdx][rightIdx] != -1) {
            return memo[leftIdx][rightIdx];
        }

        int sum = 0;

        for (int loc = leftIdx; loc < rightIdx; ++loc) {
            int leftStart = leftIdx;
            int leftEnd = loc;

            int rightStart = loc + 1;
            int rightEnd = rightIdx;

            int leftSum = prefix[leftEnd + 1] - prefix[leftStart];
            int rightSum = prefix[rightEnd + 1] - prefix[rightStart];

            if (leftSum > rightSum) {
                if (memo[rightStart][rightEnd] == -1) {
                    memo[rightStart][rightEnd] = getBestSplitSums(rightStart, rightEnd, memo, prefix, _debugDepth + 1);
                }

                sum = Math.max(sum, rightSum + memo[rightStart][rightEnd]);

            } else if (rightSum > leftSum) {
                if (memo[leftStart][leftEnd] == -1) {
                    memo[leftStart][leftEnd] = getBestSplitSums(leftStart, leftEnd, memo, prefix, _debugDepth + 1);
                }

                sum = Math.max(sum, leftSum + memo[leftStart][leftEnd]);

            } else {
                // equal sums -- Alice chooses best

                if (memo[leftStart][leftEnd] == -1) {
                    memo[leftStart][leftEnd] = getBestSplitSums(leftStart, leftEnd, memo, prefix, _debugDepth + 1);
                }

                if (memo[rightStart][rightEnd] == -1) {
                    memo[rightStart][rightEnd] = getBestSplitSums(rightStart, rightEnd, memo, prefix, _debugDepth + 1);
                }

                sum = Math.max(sum, Math.max(leftSum + memo[leftStart][leftEnd], rightSum + memo[rightStart][rightEnd]));
            }
        }

        memo[leftIdx][rightIdx] = sum;
        return sum;
    }

    public int stoneGameV(int[] stoneValue) {
        // while can divide stoneValue array in half: left=[:(stoneValue.lenth / 2)-1], right=[stoneValue.length / 2:]
        // hence [6,2,3,4,5,5] --> [6,2,3], [4,5,5]
        // Throw away the biggest summed array ([6,2,3] = 11, [4,5,5] = 14) -> ~~[4,5,5]~~
        // Repeat: 11 + [6,2,3] --> 11 + [6], [2,3] --> 11 + 5 + [2], [3] --> 11 + 5 + 2 = 18
        int[][] memo = new int[stoneValue.length][stoneValue.length];

        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        return getBestSplitSums(0, stoneValue.length - 1, memo, getPrefixSum(stoneValue), 0);
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        Solution s = new Solution();

        for (String line : Files.readAllLines(Path.of("tests.txt"))) {
            int[] nums = Arrays.stream(line.substring(1, line.length() - 1).split(",")).map(String::trim).mapToInt(Integer::parseInt).toArray();

            System.out.printf("\033[36m%s => %d\033[0m%n", Arrays.toString(nums), s.stoneGameV(nums));
        }
    }
}
