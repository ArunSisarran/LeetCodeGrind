# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
U: Checking if the trees given are identical

M: Use a dfs solution to recursively check each node and its value and if the values do not match return false otherwise return true
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False

            if (p and q) and (p.val == q.val):
                return (dfs(p.left, q.left) and dfs(p.right, q.right))

            return False
        return dfs(p, q)