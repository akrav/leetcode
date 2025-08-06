[Back to Table of Contents](../../README.md)

# Copy Linked List with Random Pointer
Difficulty: Medium

## Question
Copy Linked List with Random Pointer
Solved 
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Example 1:



Input: head = [[3,null],[7,3],[4,0],[5,1]]

Output: [[3,null],[7,3],[4,0],[5,1]]
Example 2:



Input: head = [[1,null],[2,2],[3,2]]

Output: [[1,null],[2,2],[3,2]]
Constraints:

0 <= n <= 100
-100 <= Node.val <= 100
random is null or is pointing to some node in the linked list.

## Solution Template
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #key real_node, val copy_node
        if head is None:
            return None
        node_dic = {}
        curr = head

        while curr:
            if curr not in node_dic.keys():
                copy_node = Node(x=curr.val)
                node_dic[curr] = copy_node

            if curr.next in node_dic.keys():
                node_dic[curr].next = node_dic[curr.next]
            elif curr.next:
                copy_node_next = Node(x=curr.next.val)
                node_dic[curr.next] = copy_node_next
                node_dic[curr].next = node_dic[curr.next]
            else:
                node_dic[curr].next = None
            

            if curr.random in node_dic.keys():
                node_dic[curr].random = node_dic[curr.random]
            elif curr.random:
                copy_node_random = Node(x=curr.random.val)
                node_dic[curr.random] = copy_node_random
                node_dic[curr].random = node_dic[curr.random]
            else:
                node_dic[curr].random = None
                        
            curr = curr.next
        
        for key, val in node_dic.items():
            print(f"key: {key.val}, copy: {val.val}")
            if key.next:
                print(f"key next: {key.next.val}, copy next: {val.next.val}")
            else:
                print(f"key next: {key.next}, copy next: {val.next}")

            if key.random:    
                print(f"key random: {key.random.val}, copy random: {val.random.val}")
            else:
                print(f"key random: {key.random}, copy random: {val.random}")
            print()
        
        return node_dic[head]
```
