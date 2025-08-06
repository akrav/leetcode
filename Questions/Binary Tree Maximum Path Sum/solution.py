# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1000000
        
        def dfs_max_sum(root):
            if root is None:
                return 0
            
            l = dfs_max_sum(root.left)
            r = dfs_max_sum(root.right)

            self.res = max(self.res, l+r+root.val, root.val + max(l, r, 0))

            return root.val + max(l, r, 0)
        
        dfs_max_sum(root)
        return self.res
        