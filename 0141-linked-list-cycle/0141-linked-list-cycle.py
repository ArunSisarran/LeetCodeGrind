# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
check to see if there is a cycle in a linked list, a cycle is when a node points to another previous node and the list does not end.

use a set because a set can contain no duplicates and add each referrence of the node to the set, if the set comes across a referrence it has seen already then there is a cycle
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)

            curr = curr.next

        return False
        