# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
check if a tree is height balanced meaning the heights of the two subtrees cannot differ by more than 1. 
dfs algorithm recursively finding the depth of the subtrees 
take the absoulte value of the left - right height and if its every > 1 return false
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # base case, if no node is found return tuple of True and 0
            if not root:
                return [True, 0]

            # Recursively call function on left and right trees spliting the tuple into a boolean
            # and a height variable 
            left, left_height = dfs(root.left)
            right, right_height = dfs(root.right)

            # find the max depth of the trees
            depth = 1 + max(left_height, right_height)

            # check if we are at the end of both of the subtrees, then take the abs value of the 
            # heights to check if the heights of the trees differ by more than 1
            if (left and right) and (abs(left_height - right_height) <= 1):
                balanced = True
            else:
                balanced = False

            # return a tuple with if the tree is balanced and the depth of the tree
            return [balanced, depth]

        return dfs(root)[0]

            
        