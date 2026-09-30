class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.best = 0

        l,r = 0, 1

        while r <= len(prices) - 1:
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                self.best=max(self.best, prices[r]-prices[l])
                r+=1

        return self.best