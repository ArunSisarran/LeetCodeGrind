'''
idea:
do a binary search and find the middle of the array, if the middle is bigger than the right
pointer, the array is rotated and move the left pointer to m + 1 cause we know that m can't be
the min value, if m > r then move the r pointer to just m because we can't confidently skip
m as the min value
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]
        