class Solution(object):
    def uniquePaths(self, m, n):
        if m == 0 or n == 0: return 0
        if m == 1 or n == 1: return 1
        
        graph = [[0 for col in range(n)] for row in range(m)]  # rigth way for two dimention array, not graph = [ [0] * 5 ] * 4

        for i in range(1, m):
            graph[i][0] = 1

        for j in range(1,n):
            graph[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                graph[i][j] = graph[i-1][j] + graph[i][j-1]

        
        return graph[m-1][n-1]



s = Solution()
count = s.uniquePaths(4,5)
print(count)