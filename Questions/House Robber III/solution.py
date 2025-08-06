# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def rec(node, if_can_steal):
            if node is None:
                return 0
            if (node, if_can_steal) in memo:
                return memo[(node, if_can_steal)]
            
            #take node if possible

            right_path = rec(node.right, True)
            left_path = rec(node.left, True)
            if if_can_steal == True:
                steal_right_path = rec(node.right, False)
                steal_left_path = rec(node.left, False)

                memo[(node, if_can_steal)] = max(right_path + left_path, steal_left_path + steal_right_path + node.val)

                return memo[(node, if_can_steal)]
            
            memo[(node, if_can_steal)] = left_path + right_path

            return memo[(node, if_can_steal)]
            # do not take node
        return rec(root, True)