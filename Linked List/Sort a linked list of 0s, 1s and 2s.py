# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head

        zero_head= Node(None)
        one_head= Node(None)
        two_head= Node(None)

        zero= zero_head
        one= one_head
        two= two_head
        temp= head

        while temp:
            if temp.data == 0:
                zero.next = temp
                zero = zero.next
            elif temp.data == 1:
                one.next = temp
                one = one.next
            elif temp.data == 2:
                two.next = temp
                two = two.next
            
            
            temp= temp.next

        zero.next= one_head.next if one_head.next else two_head.next
        one.next= two_head.next
        two.next= None
        
        zero_head= zero_head.next

        return zero_head

# Time Complexity: O(n) because the code iterates through the linked list once.
# Space Complexity: O(1) because the code uses a fixed number of extra variables, regardless of the input size.
    
