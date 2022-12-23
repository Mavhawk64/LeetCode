# Accepted: 04/21/2022
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        area_max = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                area_temp = self.area_of_island(grid,i,j)
                if area_temp > area_max:
                    area_max = area_temp
        return area_max
    def area_of_island(self,grid,r,c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + self.area_of_island(grid,r-1,c) + self.area_of_island(grid,r,c-1) + self.area_of_island(grid,r+1,c) + self.area_of_island(grid,r,c+1)
        