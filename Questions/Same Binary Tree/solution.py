# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs_helper(root1, root2):
            if (root1 is None and root2 is not None) or (root2 is None and root1 is not None):
                return False

            if root1 is None and root2 is None:
                return True
            
            if root1.val != root2.val:
                return False
            
            l = dfs_helper(root1.left, root2.left)
            r = dfs_helper(root1.right, root2.right)

            return l and r
        
        return dfs_helper(p, q)
            

        