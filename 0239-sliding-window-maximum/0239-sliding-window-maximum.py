'''
idea:
the window is of size k, take the max of all values within that window
'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        dq = deque()
        output = []

        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            if left > dq[0]:
                dq.popleft()

            if (right + 1) >= k:
                output.append(nums[dq[0]])
                left += 1

        return output

            


        