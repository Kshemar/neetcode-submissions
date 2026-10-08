# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter
            left, right,path = 0,0,0 #bcuz we're calc # edges not nodes 
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            path = left+right
            diameter = max(diameter, path)
            return 1+max(left, right)
        dfs(root)
        return diameter