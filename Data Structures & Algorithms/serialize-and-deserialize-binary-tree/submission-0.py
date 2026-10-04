import json

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if not root:
                res.append('N')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        def buildTree():
            nonlocal idx
            if arr[idx] == 'N':
                idx += 1
                return None
            node = TreeNode(arr[idx])
            idx += 1
            node.left = buildTree()
            node.right = buildTree()
            return node
        idx = 0
        return buildTree()