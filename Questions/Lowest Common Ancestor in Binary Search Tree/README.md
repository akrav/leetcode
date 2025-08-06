[Back to Table of Contents](../../README.md)

# Lowest Common Ancestor in Binary Search Tree
Difficulty: Medium

## Question
Lowest Common Ancestor in Binary Search Tree
Solved 
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Example 1:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
Example 2:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

Output: 3
Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

Constraints:

2 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST.

## Solution Template
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = root

        def dfs_depth(root, p, q):
            if root is None:
                return False

            l = dfs_depth(root.left, p, q)
            r = dfs_depth(root.right, p, q)

            if l and r:
                self.res = root

            if root.val == p.val or root.val == q.val:
                if l or r:
                    self.res = root    
                return True
            
            return l or r
                

        dfs_depth(root, p, q)

        return self.res


# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         res = root

#         while res:
#             if p.val > res.val and q.val > res.val:
#                 res = res.right
#             elif p.val < res.val and q.val < res.val:
#                 res = res.left
#             else:
#                 return res

        

#         return res
        
```
