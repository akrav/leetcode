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
        


        
        