# https://leetcode.com/problems/reverse-linked-list/
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Itrative Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
# Time: O(n)
# Space: O(1)

'''
# Recursive Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        # Base Case
        if not head:
            return None
        # Recursive Case
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
        
# Time: O(n)
# Space: O(n)
'''
