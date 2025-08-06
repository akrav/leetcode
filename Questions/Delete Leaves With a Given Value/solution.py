# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def rec(node, val):
            if node is None:
                return None
            
            
            node.left = rec(node.left, val)
            node.right = rec(node.right, val)

            if node.val == val and node.left is None and node.right is None:
                return None

            return node
        
        return rec(root, target)