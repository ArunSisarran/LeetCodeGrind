'''task: check if binary tree p and the binary tree q are the same

observation: for the trees to be the same the current node must be the same
and the left and right subtrees must also be the same

base cases:
if not p and not q:
    return True

if not p or not q:
    return False

check if the subtrees and if they are the same value

if (p and q) and p.val == q.val:
    return (dfs(p.left, q.left) and dfs(p.right, q.right))
else:
    return False

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if (p and q) and p.val == q.val:
                return (dfs(p.left, q.left) and dfs(p.right, q.right))
            
            return False
        return dfs(p, q)