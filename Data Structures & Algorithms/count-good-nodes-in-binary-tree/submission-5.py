# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, float("-inf"))])
        count = 0

        while q:
            node, value = q.popleft() 
            newval = max(node.val, value)
            if node.val >= value:
                count +=1
            if node.left:
                q.append((node.left, newval))
            if node.right:
                q.append((node.right, newval))
        return count
