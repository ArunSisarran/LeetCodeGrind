class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            # if this is true then we know that the array is sorted from l to m
            elif nums[m] >= nums[l]:
                # check if the target is between l and m
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # otherwise the array is sorted from m to r
            else:
                # check if the target is between r and m
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 
