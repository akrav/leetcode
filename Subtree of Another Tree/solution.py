# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        def dfs_helper(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is None or root2 is None:
                return False
            
            if root1.val != root2.val:
                return False
            
            l = dfs_helper(root1.left, root2.left)
            r = dfs_helper(root1.right, root2.right)

            return l and r
        
        def dfs_transverse_root(root1, root2):
            if root1 is None:
                return
            
            if root1.val == root2.val and self.res != True:
                self.res = self.res or dfs_helper(root1, root2)
            
            if self.res != True:
                dfs_transverse_root(root1.left, root2)
                dfs_transverse_root(root1.right, root2)
            
            return
        
        dfs_transverse_root(root, subRoot)

        return self.res

        