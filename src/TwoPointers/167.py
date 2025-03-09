class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # declaring the indicies of the left and right pointer
        l = 0
        r = len(numbers) -1

        while l < r:
            # checks the sum of the first indices
            sum = numbers[l] + numbers[r]

            # if target is reached returned the indexs +1
            if sum == target:
                return [l+1, r+1]

            # if the sum is less than the target move the left pointer up to make the number bigger
            elif sum < target:
                l += 1
            # if the sum is greater than the target move the right pointer back to make the number smaller
            else:
                r -= 1
