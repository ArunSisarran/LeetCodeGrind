class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum = 0

        for num in nums:
            sum += num

        if sum % k == 0:
            return 0
        else:
            return sum % k