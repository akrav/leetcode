[Back to Table of Contents](../README.md)

# Delete Node in a BST
Difficulty: Medium

## Question
Delete Node in a BST
Solved
Medium
Topics
premium lock icon
Companies
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105

## Solution Template
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         def rec(root, key):
#             if root is None:
#                 return None
#             if root.val == key:
#                 if root.left is None:
#                     return root.right
#                 elif root.right is None:
#                     return root.left
#                 elif root.left and root.right:
#                     # Case 3: Two children
#                     temp = root.left
#                     while temp.right:
#                         temp = temp.right
#                     root.val = temp.val
#                     root.left = rec(root.left, temp.val)
#                 else:
#                     return None
            
#             if root.val > key:
#                 rec(root.left, key)
#             elif root.val < key:
#                 rec(root.right, key)
            
#             return root
        
#         return rec(root, key)



class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def rec(node, key):
            if node is None:
                return None
            
            if key < node.val:
                node.left = rec(node.left, key)
            elif key > node.val:
                node.right = rec(node.right, key)
            else:
                #key = node thus delete
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                elif node.right is None and node.left is None:
                    return None
                else:
                    #both left and right subtrees exist
                    #find either left most value on right subtree
                    #or right most value on left subtree
                    # replace the value of our node with that value and then delete that node in the subtree

                    # go to right subtree
                    curr = node.right
                    #find smalles value
                    while curr.left:
                        curr = curr.left
                    # replace nodes value with smallest right subtree value
                    val = curr.val
                    node.val = val
                    node.right = rec(node.right, val)

                    # delete the replaced value in right subtree
            return node


        return rec(root, key)
```
