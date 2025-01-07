# https://leetcode.com/problems/merge-two-sorted-lists/
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        result = ListNode()
        rptr = result
        ll1 = list1
        ll2 = list2
        while ll1 and ll2:
            if ll1.val <= ll2.val:
                rptr.next = ll1
                rptr = ll1
                ll1 = ll1.next
            else:
                rptr.next = ll2
                rptr = ll2
                ll2 = ll2.next
        if ll1:
            rptr.next = ll1
        if ll2:
            rptr.next = ll2
        return result.next
