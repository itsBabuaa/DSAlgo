# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, ans):
        if not node:
            return None
        
        ans.append(node.val)
        self.helper(node.left, ans)
        self.helper(node.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans

# Time: O(n)
# Space: O(n)
