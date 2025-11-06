'''
Given an integer array nums return the sum of the max sub array

create a max sum variable to keep track of the largest sum
if the current_sum < 0, reset current_sum to 0
keep adding to the sum and comparing with the max sum
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:

            if current_sum < 0:
                current_sum = 0

            current_sum += num
            max_sum = max(current_sum, max_sum)

        return max_sum