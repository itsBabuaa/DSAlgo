# https://leetcode.com/problems/palindrome-linked-list/description/
'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # fn for reversing LL
        def reverseList(head):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        # Base Case
        if head == None or head.next == None:
            return True
        # Finding Mid
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        # Reversing the LL from slow
        slow.next = reverseList(slow.next)
        # moving to righthalf
        slow = slow.next
        # Comparison
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True

  # Time: O(n)
  # Space: O(1)
