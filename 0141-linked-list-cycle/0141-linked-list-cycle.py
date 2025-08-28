# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
fast and slow pointer approach

two pointers, fast pointer moves twice as fast as the slow pointer
if there is a cycle then the fast pointer will equal the slow pointer at some point
if the pointers never equal each other then there is no cycle in the linked list
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
        