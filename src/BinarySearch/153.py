class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:

            m = l + (r - l) // 2

            # if nums[m] is greater than nums[r] we know the list is rotated
            # we set l to m + 1 because we know the minimum will not be before m
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
            

            
        
