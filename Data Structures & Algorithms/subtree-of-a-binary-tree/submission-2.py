# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subroot, compare = False):
            if compare:
                if not root and not subroot:
                    return True
                if not root or not subroot:
                    return False
                if root.val != subroot.val:
                    return False
                left = dfs(root.left, subroot.left, True)
                right = dfs(root.right, subroot.right, True)
                return left and right
            if root is None:
                return False
            if dfs(root, subroot, True):
                return True
            return dfs(root.left, subroot) or dfs(root.right, subroot)

        if not subRoot:
            return True 
        return dfs(root, subRoot)