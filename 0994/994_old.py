from copy import deepcopy


class Solution:
    def has_island(self, grid: list[list[int]]) -> bool:
        # maybe try like minecraft strip-mining:
        # [dig,skip,skip,dig]

        # First, I'll just search every cell naively
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (
                    grid[i][j] == 1
                    and (grid[i - 1][j] == 0 if i > 0 else True)
                    and (grid[i][j - 1] == 0 if j > 0 else True)
                    and (grid[i + 1][j] == 0 if i < len(grid) - 1 else True)
                    and (grid[i][j + 1] == 0 if j < len(grid[i]) - 1 else True)
                ):
                    return True
        return False

    def is_spoiled_grid(self, grid: list[list[int]]) -> bool:
        return not (1 in [j for sub in grid for j in sub])

    def iterate_grid(self, grid: list[list[int]]) -> list[list[int]]:
        new_grid = deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (
                    (grid[i - 1][j] == 2 if i > 0 else False)
                    or (grid[i][j - 1] == 2 if j > 0 else False)
                    or (grid[i + 1][j] == 2 if i < len(grid) - 1 else False)
                    or (grid[i][j + 1] == 2 if j < len(grid[i]) - 1 else False)
                ):
                    new_grid[i][j] = 2
        return new_grid

    def orangesRotting(self, grid: list[list[int]]) -> int:
        if self.has_island(grid):
            return -1
        count = 0
        while not self.is_spoiled_grid(grid):
            count += 1
            grid = self.iterate_grid(grid)

        return count
