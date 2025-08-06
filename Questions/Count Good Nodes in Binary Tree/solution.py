# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs_helper(root, max_val):
            if root is None:
                return 0

            max_val = max(max_val, root.val)

            l = dfs_helper(root.left, max_val)
            r = dfs_helper(root.right, max_val)


            if root.val >= max_val:
                return l + r + 1
            return l + r
        
        return dfs_helper(root, root.val) 


            #    2
            # n     4
            #    10    8
            #         4