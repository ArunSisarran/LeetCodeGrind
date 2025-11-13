# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
given the root of a bst, return weather it is a valid bst

a valid bst must have all nodes smaller than the root to the left and all
nodes bigger than the root to the right, if this is false the bst is 
invalid.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_val, max_val):
            if not root:
                return True

            if not (min_val < root.val and max_val > root.val):
                return False

            left = dfs(root.left, min_val, root.val)
            right = dfs(root.right, root.val, max_val)

            return left and right

        return dfs(root, float('-inf'), float('inf'))
        
