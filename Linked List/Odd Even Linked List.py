# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd, even, even_head= head, head.next, head.next

        while even and even.next:
            odd.next= odd.next.next
            even.next= even.next.next

            odd= odd.next
            even= even.next

        odd.next= even_head

        return head

# Time Complexity: O(n) because the while loop iterates through the linked list once, where n is the number of nodes in the list.
# Space Complexity: O(1) as it uses a constant amount of extra space regardless of the input size.
