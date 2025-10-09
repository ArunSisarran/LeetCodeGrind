# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
idea:
use the fast and slow pointer technique to check if there is a cycle in the list, or we
could use a set and add the node to the set and if we ever see the node again we can say
there is a cycle 
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False
        