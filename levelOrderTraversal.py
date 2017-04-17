# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        
        self.results = []
        if root != None:
            return self.results
        
        q = [root]
        while q:
            new_q = []
            self.results.append([x.val for x in q])
            for node in q:
                if node.left :
                    new_q.append(node.left)
                if node.right :
                    new_q.append(node.right)
            q = new_q
        return self.results


class Solution(object):
    def levelOrderBottom(self, root):
        
        result = []
        level = 0
        
        if root == None: return result

        def widthSearch(root, level):
            while level > len(result)-1:
                result.append([])
            result[level].append(root.val)
            if root.left != None:
                widthSearch(root.left, level+1)
            if root.right != None:
                widthSearch(root.right, level+1)
        
        
        widthSearch(root,0)
        
        return  list(reversed(result))