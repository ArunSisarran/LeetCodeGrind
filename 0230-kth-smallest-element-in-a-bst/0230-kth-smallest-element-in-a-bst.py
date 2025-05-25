
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        seen = defaultdict(int)
        result = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            seen[root.val] = seen.get(root.val, 0) + 1
            inorder(root.right)

        inorder(root)

        for key, val in seen.items():
            heapq.heappush(heap, (val, key))
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])

        return result[k - 1]