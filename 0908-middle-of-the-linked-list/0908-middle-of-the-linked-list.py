# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next

        start = len(arr) // 2

        curr = head
        for i in range(start):
            curr = curr.next

        return curr