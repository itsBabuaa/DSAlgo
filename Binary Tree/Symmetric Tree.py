# https://leetcode.com/problems/symmetric-tree/description/
'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return Ture
        return self.helper(root.left, root.right)

    def helper(self, lNode, rNode):
        if lNode == None or rNode == None:
            return lNode == rNode

        if lNode.val != rNode.val:
            return False

        return self.helper(lNode.left, rNode.right) and self.helper(lNode.right, rNode.left)
