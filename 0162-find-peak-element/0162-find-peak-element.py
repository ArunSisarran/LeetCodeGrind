'''
task: find the peak element in the array and return its index

peak element is an element that is greater than both of its neigbors
array can have multiple peaks
only need to return the index of one peak doesnt matter which

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

algo must also run in O(log n) time so we cannot loop through the entire array
binary search? array not sorted
cant sort

can use the climbing a mountain appraoch to binary search, 
check if the midpoint is greater than the next element, we know that we could be a peak and move
right pointer to the mid
if we are less than the next element we know we are not a peak and move the left pointer to mid + 1
when both pointers are on the same element exit the loop and it will be on a peak index

binary search works here becaue nums[-1] = nums[n] = -â 

'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
            
        