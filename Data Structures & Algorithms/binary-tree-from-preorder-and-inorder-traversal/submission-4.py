# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {num: i for i, num in enumerate(inorder)}
        
        def buildTreeRec(pre_start, pre_end, in_start, in_end) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None
            num = preorder[pre_start]
            i = inorder_idx[num]
            node = TreeNode(num)
            left_size = i - in_start
            node.left = buildTreeRec(pre_start + 1, pre_start + left_size, in_start, i - 1)
            node.right = buildTreeRec(pre_start + left_size + 1, pre_end, i + 1, in_end)
            return node
        return buildTreeRec(0, len(preorder) - 1, 0, len(inorder) - 1)