# https://www.geeksforgeeks.org/problems/find-length-of-loop/1

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        if not head or not head.next:
            return 0

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.counter(slow, fast)
        return 0

    def counter(self, slow, fast):
        cnt = 1
        slow = slow.next

        while slow != fast:
            slow = slow.next
            cnt += 1

        return cnt
        
