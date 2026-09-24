class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.result = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.result = max(self.result, node.val + max(0,left) + max(0,right))
        
            return node.val + max(0, left, right)

        dfs(root)
        return self.result