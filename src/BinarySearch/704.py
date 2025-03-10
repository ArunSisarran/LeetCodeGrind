class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # declaring the values of left and right pointer
        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer:
            # calculate the middle value
            middle = (leftPointer + rightPointer)//2

            if nums[middle] == target:
                return middle
            # if the middle value is smaller move left to 1 more than the middle value
            elif nums[middle] < target:
                leftPointer = middle + 1
            else:
                rightPointer = middle - 1

        return -1
