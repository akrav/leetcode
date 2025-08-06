# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_idx = 0
        
        def dfs_build(preorder, inorder):
            if inorder == [] or self.preorder_idx >= len(preorder):
                return None
            
            preorder_val = preorder[self.preorder_idx]
            inorder_idx = inorder.index(preorder_val) if preorder_val in inorder else None
            if inorder_idx is None:
                return None

            root = TreeNode(preorder_val)
            left_subtree = inorder[:inorder_idx]
            right_subtree = inorder[inorder_idx+1:]
            self.preorder_idx += 1
            root.left = dfs_build( preorder, left_subtree)
            root.right = dfs_build(preorder, right_subtree)

            return root
        
        return dfs_build(preorder, inorder)
        