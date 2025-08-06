[Back to Table of Contents](../README.md)

# Reverse Nodes in K-Group
Difficulty: Hard

## Question
Reverse Nodes in K-Group
Solved 
You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:



Input: head = [1,2,3,4,5,6], k = 3

Output: [3,2,1,6,5,4]
Example 2:



Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]
Constraints:

The length of the linked list is n.
1 <= k <= n <= 100
0 <= Node.val <= 100

## Solution Template
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        count = 0
    
        def reverse(prev, head, k): # reverse linked list 2
            dummy = ListNode(0, head)
            curr = head

            l_prev = None
            count = 0
            while curr and count < k:
                next = curr.next
                curr.next = l_prev
                l_prev = curr
                curr = next
                count += 1
            if prev != None:
                prev.next = l_prev
            else:
                dummy.next = l_prev
            head.next = curr
            return dummy.next, head
        
        def can_reverse(head, k):
            count = 0
            while head and count < k:
                head = head.next
                count += 1

            if count == k:
                return True
            return False
        
        curr = head
        start = head
        count = 0

        boolf = can_reverse(curr, k)
        prev = None
        while boolf:
            # print(f"top of loop, prev: {None if prev == None else prev.val}, curr: {curr.val}")
            curr, tail = reverse(prev, curr, k)
            # print(f"curr: {curr.val}, tail: {tail}")
            if count == 0:
                start = curr

            prev = tail
            curr = tail.next
            # print(f"curr: {curr.val}, k: {k}")
            boolf = can_reverse(curr, k)
            count += 1
            # print(f"boolf: {boolf}")
        
        return start
            
```
