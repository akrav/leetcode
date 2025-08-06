[Back to Table of Contents](../README.md)

# Remove Node From End of Linked List
Difficulty: Medium

## Question
Remove Node From End of Linked List
Solved 
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

## Solution Template
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count nodes in list
        if head is None:
            return 

        list_len = 0
        temp = head
        while temp:
            list_len += 1
            temp = temp.next
        
        end_range = list_len - n 

        dummy = ListNode()
        dummy.next = head
        curr = dummy
        for i in range(end_range):
            curr = curr.next
        
        next_node = curr.next
        if next_node:
            next_node = next_node.next
        
        curr.next = next_node
        
        
        return dummy.next
        


        
        
```
