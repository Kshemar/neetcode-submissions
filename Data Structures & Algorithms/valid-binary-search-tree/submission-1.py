# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)
            if node.val > low and node.val < high:
                return left and right
            else:
                return False
        return dfs(root, float("-inf"), float("inf"))