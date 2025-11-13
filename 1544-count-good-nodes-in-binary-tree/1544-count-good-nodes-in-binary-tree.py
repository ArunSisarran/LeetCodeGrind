# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
return the number of good nodes
a node is good if from the root to the node x there are no nodes bigger than
node x.

use a dfs algorithm to go down the paths to each node.
pass in the root and a max_val param in the function.
check if the root is greater than or equal to the node we visit (max val)
recursively call that check on the left and right trees
return the total amount of good nodes
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            if not root:
                return 0

            good = 1 if root.val >= max_val else 0
            max_val = max(max_val, root.val)

            good += dfs(root.left, max_val)
            good += dfs(root.right, max_val)

            return good

        return dfs(root, root.val)