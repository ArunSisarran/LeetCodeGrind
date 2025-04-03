'''
goal: given an array calculate the least amount you need to pay to get to the end of the array

observations: you can either take 1 or 2 steps. You can start from step index 0 or step index 1
reccurrance relation? only two actions are to either take the first step or take the second step
take min(first_step, second_step)

base cases:
if n < 0:
    return 0
if n == 0 or n == 1:
    return cost[n]

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def minCost(n):
            if n < 0:
                return 0
            if n == 0 or n == 1:
                return cost[n]
            return cost[n] + min(minCost(n - 1), minCost(n - 2))
        n = len(cost)
        return min(minCost(n - 1), minCost(n - 2))