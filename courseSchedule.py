class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        if numCourses < 2 or len(prerequisites) < 2:
            return True

        while True:

            tmp = []

            mark = [True] * numCourses

            for pre in prerequisites:
                mark[pre[0]] = False

            for i in range(len(prerequisites)):
                if mark[prerequisites[i][1]]:
                    tmp.append(i)


            prerequisites = [ item for i, item in enumerate(prerequisites) if i not in tmp]

            if prerequisites == []:
                return True
            elif len(tmp) == 0:
                return False




s = Solution()


result = s.canFinish(3,[[1,0],[2,0]])

print result