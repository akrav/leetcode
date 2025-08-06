[Back to Table of Contents](../../README.md)

# Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium

## Question
Construct Binary Tree from Preorder and Inorder Traversal
Solved 
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:



Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]
Example 2:

Input: preorder = [1], inorder = [1]

Output: [1]
Constraints:

1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000

## Solution Template
```python
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
        
```
