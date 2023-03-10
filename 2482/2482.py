class Solution:
    def onesMinusZeros(self, grid):
        m = len(grid)
        n = len(grid[0])
        rowSums = [sum(grid[i]) for i in range(m)]
        transpose = [[grid[j][i] for j in range(m)] for i in range(n)]
        colSums = [sum(transpose[i]) for i in range(n)]
        output = [[2*rowSums[j] + 2*colSums[i]-m-n for i in range(n)] for j in range(m)]
        return output

x = Solution()
print(x.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))