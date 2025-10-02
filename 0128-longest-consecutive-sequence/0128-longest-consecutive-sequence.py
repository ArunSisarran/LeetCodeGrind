class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 1
        length = 1
        if not nums:
            return 0

        for i in range(len(nums) - 1):
            curr = nums[i]
            if curr + 1 == nums[i + 1]:
                length += 1
                longest = max(length, longest) 
            elif curr == nums[i + 1]:
                continue
            else:
                length = 1

        return longest

        