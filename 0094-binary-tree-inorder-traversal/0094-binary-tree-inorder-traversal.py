# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []

        def inorder(root):
            if not root:
                return None
            
            inorder(root.left)
            array.append(root.val)
            inorder(root.right)

        inorder(root)
        return array      
        
        