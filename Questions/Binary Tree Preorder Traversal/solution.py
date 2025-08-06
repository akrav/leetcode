# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rec(root):
            if root is None:
                return
            res.append(root.val)
            rec(root.left)
            rec(root.right)
            return
        
        rec(root)
        return res