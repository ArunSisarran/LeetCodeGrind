# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
U: Invert the binary tree meaning all nodes on the left hand side must go to the right hand side
if possible

M: I could do this by doing node.left = node.right on each root to swap its children

P: Create a helper function, pass in the root, swap the roots children, and recursively call that
helper function on the left and right subtrees so the nodes of those trees get swapped too
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return None

            root.left, root.right = root.right, root.left

            helper(root.left)
            helper(root.right)

        helper(root)
        return root