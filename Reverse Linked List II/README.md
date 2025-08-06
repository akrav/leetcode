[Back to Table of Contents](../README.md)

# Reverse Linked List II
Difficulty: Medium

## Question
Reverse Linked List II
Solved
Medium
Topics
premium lock icon
Companies
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?

## Solution Template
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         dummy = ListNode()
#         dummy.next = head
#         curr = head
#         prev = dummy

#         for i in range(left-1):
#             prev = curr
#             curr = curr.next
        

#         for _ in range(right - left):
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node

#             nex = curr.next
#             curr.next  = nex.next
#             nex.next = prev.next
#             prev.next = nex
            
        
#         return dummy.next




class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy

        for i in range(left-1):
            prev = curr
            curr = curr.next
        
        print(f"prev: {prev}, \ncurr: {curr}\n\n")

        #reverse
        l_prev = None
        tmp = curr
        for i in range(right-left+1):
            nex = curr.next
            curr.next = l_prev
            l_prev = curr
            curr = nex
        
        print(f"l_prev: {l_prev}, \ncurr: {curr}\n\n")

        prev.next = l_prev
        tmp.next = curr

        return dummy.next
        
```
