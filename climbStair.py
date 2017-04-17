class Solution(object):

    def climbStairs(self, n):

        if n <= 2: return n
        result = [1,2]

        for i in range(n-2):
            result.append(result[-1] + result[-2])
        return result[-1]




