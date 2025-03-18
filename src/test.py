class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:

            if num in seen:
                return True

            seen.add(num)

        return False

# O(n)
# O(n)
        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)

        for letters in s:
            map[letters] = map.get(letters, 0) + 1

        for letters in t:
            map[letters] -= 1

        for values in map.values():
            if values != 0:
                return False

        return True

# O(n)
# O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i, num in enumerate(nums):

            complement = target - num

            if complement in map:
                return (map[complement], i)

            map[num] = i

# [2,7,11,15] target = 9
# O(n)
# O(n)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = re.sub(r'[\W+_]', '', s).lower()
        newStr.replace(" ", "")
        
        l = 0
        r = len(newStr) - 1

        while l < r:

            if newStr[l] == newStr[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True

# O(n)
# O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:

            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next

        current.next = list1 if list1 else list2
        return dummy.next
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        seen = set()

        while current:

            if current in seen:
                return True

            seen.add(current)
            current = current.next
        
        return False


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l+ (r-1) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l += 1
            else:
                r -= 1

        return -1
        








