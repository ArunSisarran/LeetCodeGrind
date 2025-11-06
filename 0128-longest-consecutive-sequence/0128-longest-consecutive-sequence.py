'''
given an unsorted array of nums, return the longest consecutinve sequence

sort the array
check if the n + 1 element is 1 more than the n element
keep a max length varible
update the max length variable 
return the max length variable
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 1
        current_length = 1

        nums.sort()
        
        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                current_length += 1
                max_length = max(max_length, current_length)
            elif nums[i] == nums[i-1]:
                continue
            else:
                current_length = 1

        return max_length