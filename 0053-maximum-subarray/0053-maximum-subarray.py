class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        total_sum = 0

        for num in nums:
            if total_sum < 0:
                total_sum = 0

            total_sum += num
            curr = max(total_sum, curr)

        return curr