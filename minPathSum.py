class Solution(object):
    def minPathSum(self, grid):
        
        rowNum = len(grid)
        colNum = len(grid[0])
        

        for i in range(1,colNum):
            grid[0][i] += grid[0][i-1] 

        for i in range(1,rowNum):
            grid[i][0] += grid[i-1][0]
    
        
        for i in range(1, rowNum):
            for j in range(1, colNum):
                if grid[i-1][j] <= grid[i][j-1]:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                    
        return grid[rowNum-1][colNum-1]