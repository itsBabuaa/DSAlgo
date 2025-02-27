# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
'''
Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            self.inorder(node.right)
