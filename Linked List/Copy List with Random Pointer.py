# https://leetcode.com/problems/copy-list-with-random-pointer/description/

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
        # creating copy node b/w real LL nodes
        temp = head
        while temp:
            copyNode = ListNode(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = copyNode.next    # temp.next.next
            
        # connecting Random Pointers
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            else:
                temp.next.random = None
            temp = temp.next.next

        # extracting deepcopy LL
        dummyNode = ListNode(None)
        ptr = dummyNode
        temp = head
        while temp:
            ptr.next = temp.next    # Deep Copy
            temp.next = temp.next.next  # main LL back to real form

            ptr = ptr.next
            temp = temp.next

        return dummyNode.next
