# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        
        def dfs(node, p, q) -> (bool, bool):
            nonlocal res
            if not node:
                return (False, False)
                
            (p_left, q_left) = dfs(node.left, p, q)
            (p_right, q_right) = dfs(node.right, p, q)

            q_found = q.val == node.val or q_left or q_right
            p_found = p.val == node.val or p_left or p_right
            
            if q_found and p_found and not res:
                res = node

            print(f"{node.val}:({p_found}, {q_found})")
            return (p_found, q_found)
            
        dfs(root, p, q)
        return res


            