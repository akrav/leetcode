[Back to Table of Contents](../README.md)

# Balanced Binary Tree
Difficulty: Easy

## Question
Balanced Binary Tree
Solved 
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: true
Example 2:



Input: root = [1,2,3,null,null,4,null,5]

Output: false
Example 3:

Input: root = []

Output: true

## Solution Template
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs_height(root):
            if root is None:
                return 0

            l_depth = dfs_height(root.left)
            r_depth = dfs_height(root.right)

            if abs(l_depth - r_depth) > 1:
                self.res = False

            return max(l_depth, r_depth) + 1
        
        dfs_height(root)

        return self.res

        
```
