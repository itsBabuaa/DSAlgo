# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

        if headA == headB == None:
            return None
        
        d1 = headA
        d2 = headB

        while d1 != d2:
            if d1 == None:
                d1 = headB
            else:
                d1 = d1.next
            if d2 == None:
                d2 = headA
            else:
                d2 = d2.next
        return d1

# Time Complexity: O(m+n) where m and n are the lengths of the two linked lists.
# Space Complexity: O(1) because it uses constant extra space.
