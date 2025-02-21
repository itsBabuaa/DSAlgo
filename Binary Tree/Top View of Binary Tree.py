# https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
'''
You are given a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note: 
Return the nodes from the leftmost node to the rightmost node.
If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree,
consider the leftmost node only. 
'''

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        if not root:
            return []

        ans = []
        mpp = {}
        q = deque([(root, 0)])

        while q:
            node, line = q.popleft()

            if line not in mpp:
                mpp[line] = node.data
            
            if node.left:
                q.append((node.left, line - 1))

            if node.right:
                q.append((node.right, line + 1))

        for key in sorted(mpp.keys()):
            ans.append(mpp[key])

        return ans
