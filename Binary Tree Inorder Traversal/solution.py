# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def rec(root):
            if root is None:
                return
            rec(root.left)
            res.append(root.val)
            rec(root.right)

        rec(root)
        return res
        