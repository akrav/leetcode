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
        