# https://leetcode.com/problems/binary-tree-upside-down/

# Given a binary tree where all the right nodes are either leaf nodes with 
# a sibling (a left node that shares the same parent node) or empty, flip it 
# upside down and turn it into a tree where the original right nodes turned 
# into left leaf nodes. Return the new root.

# For example:
# Given a binary tree {1,2,3,4,5},
#     1
#    / \
#   2   3
#  / \
# 4   5
# return the root of the binary tree [4,5,2,#,#,3,1].
#    4
#   / \
#  5   2
#     / \
#    3   1  



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # [Ideas]
        # 1. use stack to reverse the tree
        if not root: return None
        
        stack, node = [], root
        # push nodes
        while node:
            stack.append([node, node.right])
            node = node.left
        print(stack)
        
        # start from bottom
        head, last = stack[-1][0], None
        while stack:
            # print(len(stack))
            node, right = stack.pop()
            node.left, node.right = None, None
            if last: 
                last.right = node
                last.left = right
            last = node
        # print(head.val)
        return head
        