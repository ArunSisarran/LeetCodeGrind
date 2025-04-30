# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(root, val):
            # If the tree is empty or null, create a node with the value of val
            if not root:
                return TreeNode(val)
            
            # If the value is greater than the root node, recursively call the right subtree
            if val > root.val:
                root.right = insert(root.right, val)
            # If the value is less than the root node, recursively call the left subtree
            elif val < root.val:
                root.left = insert(root.left, val)

            # return the head of the BST
            return root
        
        return insert(root, val)
            
