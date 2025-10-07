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
            # monotonic decreasing queue, this makes it so the 
            # highest element is always at the beginning of the queue
            # while there is a q and the last element is less than
            # the element we are putting in, pop it then add the new one
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
            
            # checks to make sure if the window is still in bounds of k, if this statement
            # is true it means that we needs to shrink our window from the left so its within k
            if left > dq[0]:
                dq.popleft()

            # checks to see if we have reached the needed size
            # add the largest element to the output and moves the window
            if (right + 1) >= k:
                output.append(nums[dq[0]])
                left += 1

        return output

            


        