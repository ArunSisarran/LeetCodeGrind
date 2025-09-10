class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def ways_to_climb_stairs(n):
            if n <= 1:
                return 1

            return ways_to_climb_stairs(n - 1) + ways_to_climb_stairs(n - 2)


        return ways_to_climb_stairs(n)

 