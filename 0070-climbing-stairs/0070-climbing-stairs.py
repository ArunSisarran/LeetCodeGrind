'''task: find how many different ways you can climb to the top of the stairs

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

you can only take 1 or 2 steps in any amount and repeat values are allowed. 
always guarenteed at least 1 stair

n = 4
1, 1, 1, 1
1, 1, 2
1, 2, 1
2, 1, 1
2, 2

step n = 4 is made up from n = 3
to get to step n we can either be n-1 stairs away or n-2 stairs away

n = n - 1 + n - 2
fib sequence

using memoization to store values 
memo = {}

create helper function

base case:
if n <= 1:
    return 1
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def ways_to_climb_stairs(n):
            if n <= 1:
                return 1

            return ways_to_climb_stairs(n - 1) + ways_to_climb_stairs(n - 2)


        return ways_to_climb_stairs(n)