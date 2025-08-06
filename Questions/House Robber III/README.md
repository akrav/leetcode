[Back to Table of Contents](../../README.md)

# House Robber III
Difficulty: Medium

## Question
House Robber III
Solved
Medium
Topics
premium lock icon
Companies
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104

## Solution Template
```python
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
```
