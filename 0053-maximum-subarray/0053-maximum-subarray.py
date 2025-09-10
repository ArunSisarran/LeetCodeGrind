class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        biggest_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += num
            biggest_sum = max(current_sum, biggest_sum)

        return biggest_sum