# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []
        def dfs(node):
            if not node:
                values.append("N")
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(values)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        index = 0
        def dfs():
            nonlocal index
            val = nodes[index]
            index+=1
            if val == "N":
                return None
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
