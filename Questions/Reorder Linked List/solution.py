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
        



        