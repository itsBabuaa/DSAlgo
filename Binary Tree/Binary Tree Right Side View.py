# https://leetcode.com/problems/binary-tree-right-side-view/description/
'''
Given the root of a binary tree,
imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        self.helper(root, 0, ans)
        return ans

    def helper(self, node, lvl, ans):
        if not node:
            return

        if lvl == len(ans):
            ans.append(node.val)
        
        self.helper(node.right, lvl + 1, ans)
        self.helper(node.left, lvl + 1, ans)
