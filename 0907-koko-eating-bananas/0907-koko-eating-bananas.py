class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0

        while l <= r:
            speed = l + (r - l) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/speed)

            if totalTime <= h:
                ans = speed
                r = speed - 1
            else:
                l = speed + 1
        return ans