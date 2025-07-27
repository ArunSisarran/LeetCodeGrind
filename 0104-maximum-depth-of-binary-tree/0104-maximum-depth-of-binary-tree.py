# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
U: Given the root of a tree, return the max depth of the tree which is the path with the most nodes connected to it 
Ex1 : is 3 because from the root to node 7 there are 3 nodes which is the largest

M: I could use a dfs algo to find the depth of the tree

P: I could create a dfs helper algorithm that takes in the root as a param. I could also make a global max value to keep track of our current longest path. The dfs algo would find the depth of the left and right subtrees and we could just take the max of those two subtrees to find what the max depth is
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            depth = max(left, right) + 1

            return depth

        return dfs(root)
