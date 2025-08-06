# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = -100000

        def dfs_search(root, k):
            if root is None:
                return 
            
            l = dfs_search(root.left, k)
            self.count += 1
            if self.count == k and self.res == -100000:
                self.res = root.val
            r = dfs_search(root.right, k)
        
        dfs_search(root, k)
        return self.res
        