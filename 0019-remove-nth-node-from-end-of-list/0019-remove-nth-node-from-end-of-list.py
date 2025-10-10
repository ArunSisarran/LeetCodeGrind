# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a new node and the .next points to the head of the list
        res = ListNode(0, head)
        # dummy node
        dummy = res

        # move the pointer n spaces after the beginning of the list
        for _ in range(n):
            head = head.next
        
        # while head is valid move head and dummy node, this makes it so when head 
        # reaches the end of the list, the dummy node will be pointing to the node 
        # right before the node that needs to be removed, this is because dummy is currently 
        # its own node, then when head goes to the end of the list, dummy will be at n - 1
        # nodes from the end which is the node before the node to be removed
        while head:
            head = head.next
            dummy = dummy.next
        
        # set the node before the nth node to skip over that node
        dummy.next = dummy.next.next

        # return the head of the list
        return res.next
