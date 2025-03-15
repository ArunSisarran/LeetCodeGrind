# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # call the ListNode class to make a dummy node that will act as out head
        d = ListNode()
        # have another variable tha points to the dummy node
        curr = d

        # while there are still node in list 1 and list 2
        while list1 and list2:

            # if the value in list 1 is less than list 2
            # set the curr.next value to the node in list1
            # set the curr variable to point to list1
            # have list1 move to its next node
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            # else that means list 2 node value is smaller
            # set the curr.next value to list 2
            # set curr to list 2
            # have list 2 move to its next node
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        # this says that after the while loop ends it means one of the linked list or both
        # no longer has any nodes. So set curr.next equal to whichever list still has nodes
        # and if both no longer have nodes this gets set to None
        curr.next = list1 if list1 else list2

        # return d.next because curr was what we used to iterate through the linked list
        # but d was are dummy node that acts as the head and d.next would be the first value
        # in the sorted linked list because d points to nothing
        return d.next
