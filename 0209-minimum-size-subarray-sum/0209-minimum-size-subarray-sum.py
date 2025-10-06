'''
idea:
start the window on the first element and exand the window until the sum is greater
than or equal to the target. If the window is greater than the target lessen the left
side of the window until it is equal to or less than the target. Return the smallest 
sub array length found
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        smallest = float('inf')
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                smallest = min(smallest, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return smallest if smallest != float('inf') else 0


        