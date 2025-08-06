# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs_search(root, left, right):
            if root is None:
                return True
            if root.val <= left or root.val >= right:
                return False
            
            l = dfs_search(root.left, left, root.val)
            r = dfs_search(root.right, root.val, right)

            return l and r
        
        return dfs_search(root, -100000, 100000)

            

        