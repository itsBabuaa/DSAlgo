# https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1

'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        if not root or not root.next:
            return root

        newHead = self.flatten(root.next)

        head = self.merge(root, newHead)

        return head

    def merge(self, list1, list2):
        dummy = Node(None)
        res = dummy

        while list1 and list2:
            if list1.data < list2.data:
                res.bottom = list1
                res = list1
                list1 = list1.bottom
            else:
                res.bottom = list2
                res = list2
                list2 = list2.bottom
            
            res.next = None

        if list1:
            res.bottom = list1
        else:
            res.bottom = list2

        if dummy.bottom:
            dummy.bottom.next = None

        return dummy.bottom
