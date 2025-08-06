# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs_height(root):
            if root is None:
                return 0

            l_depth = dfs_height(root.left)
            r_depth = dfs_height(root.right)

            if abs(l_depth - r_depth) > 1:
                self.res = False

            return max(l_depth, r_depth) + 1
        
        dfs_height(root)

        return self.res

        