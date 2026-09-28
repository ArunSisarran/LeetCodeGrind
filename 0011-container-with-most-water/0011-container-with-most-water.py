class Solution:
    def maxArea(self, height: list[int]) -> int:
        self.best = float('-inf')
        l = 0
        r = len(height) - 1
        
        while l < r:

            area = min(height[l], height[r]) * (r - l) 
            self.best = max(self.best, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return self.best