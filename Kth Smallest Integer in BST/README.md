[Back to Table of Contents](../README.md)

# Kth Smallest Integer in BST
Difficulty: Medium

## Question
Kth Smallest Integer in BST
Solved 
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:



Input: root = [2,1,3], k = 1

Output: 1
Example 2:



Input: root = [4,3,5,2,null], k = 4

Output: 5
Constraints:

1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000

## Solution Template
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = -100000

        def dfs_search(root, k):
            if root is None:
                return 
            
            l = dfs_search(root.left, k)
            self.count += 1
            if self.count == k and self.res == -100000:
                self.res = root.val
            r = dfs_search(root.right, k)
        
        dfs_search(root, k)
        return self.res
        
```
