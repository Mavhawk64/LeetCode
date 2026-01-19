// Accepted: 01/18/2026
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
       int m = mat.length;
       int n = mat[0].length;

        // Hint 1: Store prefix sum of all grids in another 2D array.
        int[][] prefixSum = new int[m + 1][n + 1];
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                prefixSum[i][j] = mat[i - 1][j - 1]
                        + prefixSum[i - 1][j]
                        + prefixSum[i][j - 1]
                        - prefixSum[i - 1][j - 1];
            }
        }

        // Hint 2: Try all possible solutions and if you cannot find one, return 0.
        // Hint 3. If x is a valid answer, then any y < x is also a valid answer.
        // Use a binary search to find the answer.
        int left = 1;
        int right = Math.min(m, n);
        while (left <= right) {
            int mid = left + (right - left) / 2;
            boolean found = false;
            for (int i = mid; i <= m; ++i) {
                for (int j = mid; j <= n; ++j) {
                    int total = prefixSum[i][j]
                            - prefixSum[i - mid][j]
                            - prefixSum[i][j - mid]
                            + prefixSum[i - mid][j - mid];
                    if (total <= threshold) {
                        found = true;
                        break;
                    }
                }
                if (found) {
                    break;
                }
            }
            // Binary search adjustment
            if (found) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return right;
    }
}

class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        // [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
        // 4
        // [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
        // 1
        int[][] mat = {
                {1, 1, 3, 2, 4, 3, 2},
                {1, 1, 3, 2, 4, 3, 2},
                {1, 1, 3, 2, 4, 3, 2}
        };
        int threshold = 4;
        System.out.println(s.maxSideLength(mat, threshold)); // Expected: 2
        mat = new int[][]{
                {2, 2, 2, 2, 2},
                {2, 2, 2, 2, 2},
                {2, 2, 2, 2, 2},
                {2, 2, 2, 2, 2},
                {2, 2, 2, 2, 2}
        };
        threshold = 1;
        System.out.println(s.maxSideLength(mat, threshold)); // Expected: 0
    }
}