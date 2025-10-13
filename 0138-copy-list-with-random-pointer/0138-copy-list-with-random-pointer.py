"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # creates a hashmap to store the nodes
        hashmap = {None:None}
        curr = head

        # loop through the linked list and copies all the linked list nodes values
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        # loops through the linked list again but this time sets all the connections of the nodes
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next

        # return the head of the deep copy list
        return hashmap[head]
        