
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
goal: given the root of a BST, and a int k, return the k smallest value in the tree

root = [3,1,4,null,2], k = 1
1

root = [5,3,6,2,4,null,null,1], k = 3
3

implement a preorder DFS
use hashmap to keep track of values
add values to a heap
pop the k smallest values to an array
return the array at index k - 1
'''


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        seen = defaultdict(int)
        result = []

        def dfs(root):
            if not root:
                return
            nonlocal seen
            dfs(root.left)
            seen[root.val] = seen.get(root.val, 0) + 1
            dfs(root.right)

        dfs(root)

        for key, val in seen.items():
            heapq.heappush(heap, (val, key))
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])

        return result[k - 1]