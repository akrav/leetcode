[Back to Table of Contents](../README.md)

# Diameter of Binary Tree
Difficulty: Easy

## Question
Diameter of Binary Tree
Solved 
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:



Input: root = [1,null,2,3,4,5]

Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:

Input: root = [1,2,3]

Output: 2
Constraints:

1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

## Solution Template
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def max_depth(root):
            if root is None:
                return 0
            
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)

            self.res = max(self.res, left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        
        if root is None:
            return 0

        max_depth(root)

        return self.res


            
```
