# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
loop through the linked list to find its length
subtract length - n to see where in the list we need to remove the node
go to the node right before it and set its next pointer to .next.next
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        remove = length - n

        if remove == 0:
            return head.next

        curr = head

        for _ in range(remove - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head

