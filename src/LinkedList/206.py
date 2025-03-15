# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current and previous values
        curr = head
        prev = None

        while curr:
        
            # setting up a temp value to keep track of the next value in the original list
            temp = curr.next
            # setting current.next to previous because we are reversing the list
            curr.next = prev
            # setting previous to current because we are going to continue iterating through the list
            prev = curr
            # setting the current node to the temp node so we can continue going through the list
            curr = temp

        # return the previous because this is the new head
        return prev

