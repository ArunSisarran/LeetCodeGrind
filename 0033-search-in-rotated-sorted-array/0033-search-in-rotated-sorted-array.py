
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            # if this is true the array is sorted from l to m
            elif nums[m] >= nums[l]:
                # check if the target is in the range from l to m
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # if we are here it mean the array is sorted from m to r
            else:
                # check if target is in range m to r
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 
        