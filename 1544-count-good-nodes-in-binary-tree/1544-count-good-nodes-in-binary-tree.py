# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, curr):
            if not node:
                return 0
            if node.val >= curr:
                self.count += 1
                curr = node.val
            dfs(node.left, curr)
            dfs(node.right, curr)
        
        dfs(root, root.val)
        return self.count
        
