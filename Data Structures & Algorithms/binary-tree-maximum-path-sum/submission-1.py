# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def pathSum(node):
            nonlocal max_sum
            if not node:
                return 0
            sum_node_left = pathSum(node.left)
            sum_node_right = pathSum(node.right)
            max_sum = max(max_sum, node.val + max(sum_node_left, 0) + max(sum_node_right, 0))
            return max(node.val + max(sum_node_left, 0), node.val + max(sum_node_right, 0))
        
        max_sum = root.val
        pathSum(root)
        return max_sum
        