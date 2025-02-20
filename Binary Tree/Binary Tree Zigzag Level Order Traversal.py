# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = deque([root])
        leftToRight = True

        while q:
            size = len(q)
            temp = []
            for i in range(size):
                
                node = q.popleft()

                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(temp) if leftToRight else res.append(temp[::-1])
            leftToRight = not leftToRight

        return res
