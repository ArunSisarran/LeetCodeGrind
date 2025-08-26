# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Flip the left and right nodes
recursively call the left and right tree 
dfs algorithm
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return 0

            root.left, root.right = root.right, root.left

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root

        