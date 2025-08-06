[Back to Table of Contents](../../README.md)

# Binary Tree Maximum Path Sum
Difficulty: Hard

## Question
Binary Tree Maximum Path Sum
Solved 
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:



Input: root = [1,2,3]

Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:



Input: root = [-15,10,20,null,null,15,5,-5]

Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:

1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000

## Solution Template
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1000000
        
        def dfs_max_sum(root):
            if root is None:
                return 0
            
            l = dfs_max_sum(root.left)
            r = dfs_max_sum(root.right)

            self.res = max(self.res, l+r+root.val, root.val + max(l, r, 0))

            return root.val + max(l, r, 0)
        
        dfs_max_sum(root)
        return self.res
        
```
