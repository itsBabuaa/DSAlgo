# https://leetcode.com/problems/sort-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.getMid(head)

        left = head
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMid(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        dummy = ListNode(None)
        res = dummy

        while left and right:
            if left.val >= right.val:
                res.next = right
                right = right.next
            else:
                res.next = left
                left = left.next

            res = res.next
        
        if left:
            res.next = left
        else:
            res.next = right

        return dummy.next
