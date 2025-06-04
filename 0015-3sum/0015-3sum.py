class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            else:
                l = index + 1
                r = len(nums) - 1

                while l < r:
                    three_sum = value + nums[l] + nums[r]

                    if three_sum > 0:
                        r -= 1
                    elif three_sum < 0:
                        l += 1
                    else:
                        result.append([value, nums[l], nums[r]])
                        # keep it moving
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

        return result