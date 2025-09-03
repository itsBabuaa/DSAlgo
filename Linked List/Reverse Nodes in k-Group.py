# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:
            Kth = self.getKth(grpPrev, k)
            if not Kth:
                break
            grpNxt = Kth.next

            # reverse grp
            prev, curr = Kth.next, grpPrev.next
    
            while curr != grpNxt:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
    
            temp = grpPrev.next
            grpPrev.next = Kth
            grpPrev = temp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


# Time Complexity: O(n) where n is the number of nodes in the linked list. getKth takes O(k), the outer while loop iterates n/k times, and the inner while loop (reversing the group) takes O(k). Thus O((n/k)*k) = O(n)
# Space Complexity: O(1) because the algorithm uses a constant amount of extra space, regardless of the input size. Variables like dummy, grpPrev, Kth, prev, curr, and temp use constant space.
