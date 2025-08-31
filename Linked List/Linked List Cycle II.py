# https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        fast = head
        slow = head
        cycleHead = head

        # finding cycle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:    # cycle found
            
                while cycleHead != slow:  # Finding cycle's start
                    cycleHead = cycleHead.next
                    slow = slow.next

                return cycleHead

        return None

# Time Complexity: O(n), where n is the number of nodes in the linked list. The while loops iterate through the list to find the cycle and the starting point of the cycle.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space regardless of the input size (only a few pointers).
