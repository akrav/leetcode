[Back to Table of Contents](../README.md)

# Subtree of Another Tree
Difficulty: Easy

## Question
Subtree of Another Tree
Solved 
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:



Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true
Example 2:



Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false
Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100

## Solution Template
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        def dfs_helper(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is None or root2 is None:
                return False
            
            if root1.val != root2.val:
                return False
            
            l = dfs_helper(root1.left, root2.left)
            r = dfs_helper(root1.right, root2.right)

            return l and r
        
        def dfs_transverse_root(root1, root2):
            if root1 is None:
                return
            
            if root1.val == root2.val and self.res != True:
                self.res = self.res or dfs_helper(root1, root2)
            
            if self.res != True:
                dfs_transverse_root(root1.left, root2)
                dfs_transverse_root(root1.right, root2)
            
            return
        
        dfs_transverse_root(root, subRoot)

        return self.res

        
```
