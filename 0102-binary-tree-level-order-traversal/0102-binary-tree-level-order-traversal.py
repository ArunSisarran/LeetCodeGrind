# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
return the level order traversal of the binary tree

use a bfs algorithm
use a double ended queue
add the root of the tree to the queue
while the q exists:
make an array to show what nodes are on the same level
pop the left side of the queue
append that nodes value to the same level array
if the node has a left child, put it in the queue
if the node has a right child, put it in the queue
append the same level array to the result array
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        q = deque()
        q.append(root)

        while q:
            same_level = []

            for _ in range(len(q)):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(same_level)

        return result

        