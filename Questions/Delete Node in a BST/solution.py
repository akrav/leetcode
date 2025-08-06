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