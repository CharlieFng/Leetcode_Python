class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        rowNum = len(obstacleGrid)
        colNum = len(obstacleGrid[0])

        for i in range(rowNum):
            for j in range(colNum):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        if obstacleGrid[0][0] == -1:
            return 0
        else:
            obstacleGrid[0][0] = 1

        for i in range(1, rowNum):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            elif obstacleGrid[i][0] == -1:
                for j in range(i + 1, rowNum):
                    obstacleGrid[j][0] = -1
                break

        for i in range(1, colNum):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            elif obstacleGrid[0][i] == -1:
                for j in range(i + 1, colNum):
                    obstacleGrid[0][j] = -1

        for i in range(1, rowNum):
            for j in range(1, colNum):
                if obstacleGrid[i][j] != -1:
                    if obstacleGrid[i - 1][j] != -1 and obstacleGrid[i][j - 1] != -1:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                    elif obstacleGrid[i - 1][j] != -1:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                    elif obstacleGrid[i][j - 1] != -1:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                    else:
                        obstacleGrid[i][j] = -1

        return 0 if obstacleGrid[rowNum - 1][colNum - 1] == -1 else obstacleGrid[rowNum-1][colNum-1]


