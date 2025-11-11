# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
return the right side view of the binary tree
if the tree has a right side return all the nodes on the right side 
and right subtree on the right, but if that doesn't exist return the left subtree
if both those dont exist return the left right side.

right right - right left - left right - left left
return the last value in the queue at every level because that would be the 
rightmost node
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        q = deque()
        q.append(root)

        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                if i == level_length - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return result