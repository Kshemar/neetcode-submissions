# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curmax):
            if not node:
                return 0
            good = 1 if node.val >= curmax else 0
            newmax = max(curmax, node.val)
            return good + dfs(node.left, newmax) + dfs(node.right, newmax)
        return dfs(root, root.val)