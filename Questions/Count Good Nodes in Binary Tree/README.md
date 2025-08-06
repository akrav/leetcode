[Back to Table of Contents](../../README.md)

# Count Good Nodes in Binary Tree
Difficulty: Medium

## Question
Count Good Nodes in Binary Tree
Solved 
Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:



Input: root = [2,1,1,3,null,1,5]

Output: 3


Example 2:

Input: root = [1,2,-1,3,4]

Output: 4
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
    def goodNodes(self, root: TreeNode) -> int:

        def dfs_helper(root, max_val):
            if root is None:
                return 0

            max_val = max(max_val, root.val)

            l = dfs_helper(root.left, max_val)
            r = dfs_helper(root.right, max_val)


            if root.val >= max_val:
                return l + r + 1
            return l + r
        
        return dfs_helper(root, root.val) 


            #    2
            # n     4
            #    10    8
            #         4
```
