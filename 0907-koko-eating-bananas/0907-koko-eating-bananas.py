class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(speed):
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / speed)
            return totalTime <= h

        l = 1
        r = max(piles)
        ans = 0

        while l <= r:
            speed = l + (r - l) // 2

            if canEat(speed):
                ans = speed
                r = speed - 1
            else:
                l = speed + 1

        return ans