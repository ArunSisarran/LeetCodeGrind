# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, current_max):
            if not root:
                return 0

            if root.val >= current_max:
                good = 1
                current_max = root.val
            else:
                good = 0

            left = dfs(root.left, current_max)
            right = dfs(root.right, current_max)

            total = good + left + right

            return total

        return dfs(root, root.val)