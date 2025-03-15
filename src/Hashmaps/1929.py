class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (2 * length)

        for i in range(length):
            ans[i] = nums[i]
            ans[i+1] = nums[i]

        return ans

