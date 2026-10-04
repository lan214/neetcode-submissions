# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node) -> (bool, int):
            if not node:
                return (True, 0)
            
            balancedLeft, left = dfs(node.left)
            balancedRight, right = dfs(node.right)
            balanced = balancedLeft and balancedRight and abs(left - right) <= 1
            return (balanced, 1 + max(left, right))

        return dfs(root)[0]
