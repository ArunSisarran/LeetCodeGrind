'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

base case:
if not node:
    return 0 cause it has no depth

get the heights of the left and right subtrees
recursively call the trees

left = dfs(node.left)
right = dfs(node.right)

find the length of those trees from where we currently are

length = max(left, right) + 1

return length
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_tree = dfs(node.left)
            right_tree = dfs(node.right)

            length = max(left_tree, right_tree) + 1
            return length

        return dfs(root)
    