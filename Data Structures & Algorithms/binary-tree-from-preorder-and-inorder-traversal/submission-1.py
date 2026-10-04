# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {num: i for i, num in enumerate(inorder)}
        current_idx = 0
        def buildTreeRec(left: int, right: int):
            nonlocal current_idx
            if left > right or current_idx >= len(preorder):
                return None

            num = preorder[current_idx]
            if inorder_idx[num] > right or inorder_idx[num] < left:
                return None

            node = TreeNode(num)

            current_idx += 1
            node.left = buildTreeRec(left, inorder_idx[num] - 1)
            node.right = buildTreeRec(inorder_idx[num] + 1, right)

            return node
            
        return buildTreeRec(0, len(inorder) - 1)
