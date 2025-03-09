class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list to make it easier to find duplicates
        nums.sort()
        n = len(nums)
        ans = []

        # loop through the list 
        for i in range(n):
            # if nums > 0 than no answer can produce a value of 0
            if nums[i] > 0:
                break
            # if the previous value is the same as the current index skip it
            elif i > 0 and nums[i] == nums[i - 1]:
                continue

            leftPointer = i + 1
            rightPointer = n - 1

            while leftPointer < rightPointer:
                sum = nums[i] + nums[leftPointer] + nums[rightPointer]

                # if the sum == 0 then add it to the ans array
                if sum == 0:
                    ans.append([nums[i], nums[leftPointer], nums[rightPointer]])
                    leftPointer, rightPointer = leftPointer + 1, rightPointer - 1
                    # if the leftpointer is a duplicate of its previous value increment it again
                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                        leftPointer += 1
                    # if the rightpointer is a duplicate of its previous value increment it again
                    while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer + 1]:
                        rightPointer -= 1

                elif sum < 0:
                    leftPointer += 1
                else:
                    rightPointer -= 1

        return ans
