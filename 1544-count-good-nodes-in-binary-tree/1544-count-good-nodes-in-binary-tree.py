# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, val):
            if not root:
                return 0

            if root.val >= val:
                good = 1
                val = root.val
            else:
                good = 0

            left = dfs(root.left, val)
            right = dfs(root.right, val)

            total = good + left + right

            return total

        return dfs(root, root.val)
            
