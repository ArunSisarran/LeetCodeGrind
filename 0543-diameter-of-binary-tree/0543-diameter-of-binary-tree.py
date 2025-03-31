'''Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

find the length of the longest path

base case:
if not node:
    return 0

check the height of the tree from current node

left = dfs(node.left)
right = dfs(node.right)

length = max(left, right) + 1

need to keep track of what the current longest length is 

self.longest_path as a global variable

update longest_path if the length is greater than the current longest path

longest_path = max(long_path, left + right)

return length

return longest_path in main function
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest_path = max(self.longest_path, left + right)
            length = 1 + max(left, right)
            return length

        dfs(root)
        return self.longest_path
        