'''
return the maximum number you can obtain if you bought a stock on prices[i] and sold it on prices[i + n].

compare adjacent values if prices[i] is greater than prices[i + 1] don't buy the stock
if prices[i] is less than prices[i + 1] buy the stock and save the potential profit in a variable if you sold it at prices[i + 1]
continue moving along the array, checking if we can get a larger profit, at the end return that variable we saved out max profit in
if there was never any profit return 0
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_money = 0

        l = 0
        r = 1

        while r <= len(prices) - 1:
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                max_money = max(profit, max_money)
                r += 1

        return max_money
        