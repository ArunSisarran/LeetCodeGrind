# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min, max):
            if not node:
                return True

            if not (node.val > min and node.val < max):
                return False

            return dfs(node.left, min, node.val) and dfs(node.right, node.val, max)
        
        return dfs(root, float('-inf'), float('inf'))