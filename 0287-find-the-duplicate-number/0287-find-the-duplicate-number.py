class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using the fast and slow pointer approach, these pointers will find a cycle 
        # in the array which means there is a duplicate value
        slow = nums[0]
        fast = nums[0]

        # finding the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]

        # Without this second loop, we would have detected the presence of a cycle but would not have 
        # determined the duplicate element. The second loop is essential for identifying the 
        # duplicate element within the cycle.
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

'''
[3,1,3,4,2]

slow = 3
fast = 3

slow = 4
fast = 2

slow = 2
fast = 4

slow = 3
fast = 3
'''

        