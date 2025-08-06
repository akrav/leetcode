[Back to Table of Contents](../README.md)

# Reorder Linked List
Difficulty: Medium

## Question
Reorder Linked List
Solved 
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000

## Solution Template
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return

        #find midpoint
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        

        #reverse second half
        head2 = slow
        prev.next = None
        prev = None

        while head2:
            next_node = head2.next
            head2.next = prev
            prev = head2
            head2 = next_node
        
        #merge linklist
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        head1 = head
        head2 = prev

        is_odd = True
        while head1 and head2:

            if is_odd:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            
            curr = curr.next
            is_odd = not is_odd

        
        if head1:
            curr.next = head1
        
        if head2:
            curr.next = head2
        



        
```
