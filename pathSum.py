class Solution(object):
    def hasPathSum(self, root, sum):

        result = False

        def depthSearch(root, num):
            global result

            if root.left == None and root.right == None:
                result = ((root.val == num) or result)

            if root.left != None:
                depthSearch(root.left, num - root.val)

            if root.right != None:
                depthSearch(root.right, num - root.val)

        if root == None: return False

        depthSearch(root, sum)
        return result



s = Solution()

s.