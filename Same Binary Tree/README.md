[Back to Table of Contents](../README.md)

# Same Binary Tree
Difficulty: Easy

## Question
Same Binary Tree
Solved 
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:



Input: p = [1,2,3], q = [1,2,3]

Output: true
Example 2:



Input: p = [4,7], q = [4,null,7]

Output: false
Example 3:



Input: p = [1,2,3], q = [1,3,2]

Output: false
Constraints:

0 <= The number of nodes in both trees <= 100.
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs_helper(root1, root2):
            if (root1 is None and root2 is not None) or (root2 is None and root1 is not None):
                return False

            if root1 is None and root2 is None:
                return True
            
            if root1.val != root2.val:
                return False
            
            l = dfs_helper(root1.left, root2.left)
            r = dfs_helper(root1.right, root2.right)

            return l and r
        
        return dfs_helper(p, q)
            

        
```
