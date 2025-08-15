class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            # check if the current value is the same as the previous and if it is skip it
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                l, r = i + 1, len(nums) - 1

                while l < r:
                    
                    if nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    else:
                        result.append([nums[i], nums[l], nums[r]])
                        # move the left pointer to continue looking for more tuples that equal 0
                        l += 1
                        
                        # if the left pointer is the same value as the previous left pointer
                        # move it because we don't want duplicates
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

        return result

#O(n^2)
#O(n)