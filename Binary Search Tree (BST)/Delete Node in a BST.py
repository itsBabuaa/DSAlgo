# https://leetcode.com/problems/delete-node-in-a-bst/
'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        def helper(root):
            
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left

            rChild = root.right
            #last_child is the right most child of the left sub tree
            last_child = root.left
            while last_child.right:
                last_child = last_child.right

            last_child.right = rChild
            
            return root.left

        if root.val == key:
            return helper(root)

        node = root
        while node:
            if node.val > key:
                if node.left and node.left.val == key:
                    node.left = helper(node.left)
                    break
                else:
                    node = node.left
            else:
                if node.right and node.right.val == key:
                    node.right = helper(node.right)
                    break
                else:
                    node = node.right
        return root
