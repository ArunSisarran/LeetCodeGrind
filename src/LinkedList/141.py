# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        # make a set to add all the nodes we pasted
        seen = set()

        while curr:

            # if the node is already in the set we know the linked list is a cycle
            if curr in seen:
                return True

            # if its not in the set add it
            seen.add(curr)

            curr = curr.next

        # if it exited the while loop we know there is an end to the list
        return False

    # O(n) time


# Another way in O(1) space
# This uses rabbit and tourtoise algo
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = ListNode()
        d.next = head
        slow = d
        fast = d

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True

        return False
