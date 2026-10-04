# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_so_far):
            if not root:
                return 0
            res = 0
            if root.val >= max_so_far:
                res = 1
                max_so_far = root.val
            return res + dfs(root.left, max_so_far) + dfs(root.right, max_so_far)

        return dfs(root, root.val)
            
