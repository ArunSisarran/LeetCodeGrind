'''
Given the root of a binary tree, invert the tree, and return its root.
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

all nodes are switched with the nodes on the opposite side.
left is switched with right and vise versa.

node.left, node.right = node.right, node.left

base case:
if the the node doesnt exist return nothing
if not node:
    return None

recursively call the tree

left = dfs(node.left)
right = dfs(node.right)

return root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            node.left, node.right = node.right, node.left

            left = dfs(node.left)
            right = dfs(node.right)

            return node

        dfs(root)
        return root