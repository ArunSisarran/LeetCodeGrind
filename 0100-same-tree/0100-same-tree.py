# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
idea:
traverse the tree using a dfs algo and compare the left and right substrees recursively
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # checking if both trees exists or don't exisit
            if not p and not q:
                return True
            
            if (p and not q) or (not p and q):
                return False
            
            # check both nodes exists and that their values equal each other
            if (p and q) and (p.val == q.val):
                # return if the left and right trees also equal each other
                return (dfs(p.left, q.left) and dfs(p.right, q.right))

            # default condition if there is a case where they don't match up
            return False

        return dfs(p, q)