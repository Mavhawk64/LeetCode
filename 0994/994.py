# Accepted: 08/31/2026
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # before, we were iterating fairly naively with going through each cell.
        # now, we can optimize it by finding the positions of all the 2's
        # possible other optimization is turning a dead cell to 3? This happens after an orange has rotted its neighbors
        rotten = []  # stored as (i, j)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
        iterations = 0
        while len(rotten) > 0:
            iterations += 1
            new_rotten = []
            for idx in range(len(rotten)):
                # strictly append new rottens, old rottens die.
                i, j = rotten[idx]
                grid[i][j] = 3
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    new_rotten.append((i - 1, j))
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    new_rotten.append((i, j - 1))
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    new_rotten.append((i + 1, j))
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    new_rotten.append((i, j + 1))
            rotten = new_rotten
        # Check if there are any untouched fruit:
        if 1 in [j for sub in grid for j in sub]:
            return -1
        return max(0, iterations - 1)


if __name__ == "__main__":
    s = Solution()
    grids = [
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 2]],
        [[1], [1], [1], [1]],
    ]
    for grid in grids:
        print(s.orangesRotting(grid))
