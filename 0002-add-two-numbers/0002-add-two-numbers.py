# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node that will act as our new linked list
        dummy = ListNode()
        curr = dummy
        # the current sum and the carry variable start at 0
        sum = carry = 0

        # while either list exists or we have a carry variable
        while l1 or l2 or carry:
            # add the carry variable to our current sum
            sum = carry

            # if list 1 exists, add its node value to the sum
            if l1:
                sum += l1.val
                l1 = l1.next
            # if list 2 exists add its node value to the sum
            if l2:
                sum += l2.val
                l2 = l2.next

            # the number we add will be the second digit of a two digit number if there is one and we
            # carry the remainder, if its a one digit number we just add that number and carry nothing
            # Ex1. sum = 12, 12 % 10 = 2, we set the nodes value to 2 and carry the 1
            # Ex2. sum = 9, 9 % 10 = 9, we set the nodes value to 9 and carry nothing
            num = sum % 10
            carry = sum // 10

            # add the new node with its value to our new linked list
            curr.next = ListNode(num)
            curr = curr.next

        # return the head of our new linked list
        return dummy.next
            

        