# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpath = float("-inf")
        def dfs(node):
            nonlocal maxpath
            if  not node:
                return 0
            left = max(0,dfs(node.left)) #find max path on lhs
            right = max(0, dfs(node.right)) #find max path on rhs
            path = node.val+left+right
            maxpath = max(maxpath, path)
            return node.val + max(left,right)
        dfs(root)
        return maxpath