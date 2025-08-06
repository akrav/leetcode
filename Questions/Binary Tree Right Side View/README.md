[Back to Table of Contents](../../README.md)

# Binary Tree Right Side View
Difficulty: Medium

## Question
Binary Tree Right Side View
Solved 
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:



Input: root = [1,2,3]

Output: [1,3]
Example 2:



Input: root = [1,2,3,4,5,6,7]

Output: [1,3,7]
Constraints:

0 <= number of nodes in the tree <= 100
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = [root]
        result = []

        while q:
            level_size = len(q)
            result.append(q[-1].val)

            for i in range(level_size):
                curr = q.pop(0)

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
        return result

         
         
```
