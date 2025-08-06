# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = root

        def dfs_depth(root, p, q):
            if root is None:
                return False

            l = dfs_depth(root.left, p, q)
            r = dfs_depth(root.right, p, q)

            if l and r:
                self.res = root

            if root.val == p.val or root.val == q.val:
                if l or r:
                    self.res = root    
                return True
            
            return l or r
                

        dfs_depth(root, p, q)

        return self.res


# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         res = root

#         while res:
#             if p.val > res.val and q.val > res.val:
#                 res = res.right
#             elif p.val < res.val and q.val < res.val:
#                 res = res.left
#             else:
#                 return res

        

#         return res
        