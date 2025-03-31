class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Keep track of the amount of moves needed
        counter = 0
        # Sort the array to make it easier to find values that need to be incremented
        nums = sorted(nums)
        print(nums)

        # Start at the first index
        for i in range(1, len(nums)):
            # If it is the same as the previous value increment it by 1 more than the previous
            if nums[i] <= nums[i-1]:
                # Calculate count by adding one more of the previous and subtracting the current
                counter += (nums[i-1] + 1) - nums[i]
                nums[i] = nums[i-1] + 1

        return counter



