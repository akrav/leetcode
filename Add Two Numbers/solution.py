# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_list(l):
            prev = None

            while l:
                next_node = l.next
                l.next = prev
                prev = l
                l = next_node
            
            return prev
        

        def add_lists(list_1, list_2):
            carry = 0
            new_val = list_1.val + list_2.val + carry
            carry = new_val // 10
            remainder = new_val % 10
            prev = ListNode(remainder)
            head = prev

            list_1 = list_1.next
            list_2 = list_2.next
            
            while list_1 or list_2:
                list1_val = 0
                if list_1:
                    list1_val = list_1.val
                
                list2_val = 0
                if list_2:
                    list2_val = list_2.val

                new_val = list1_val + list2_val + carry
                carry = new_val // 10
                remainder = new_val % 10
                node = ListNode(remainder)

                prev.next = node
                prev = node

                if list_1:
                    list_1 = list_1.next
                if list_2:
                    list_2 = list_2.next
            
            if carry == 1:
                node = ListNode(1)
                prev.next = node
                prev = node

            
            return head
        return add_lists(l1, l2)


# l1=[9,9,9,9,9,9,9]
# l2=[9,9,9,9]
#    [8,]
#    9 + 9 + carry 0 = 18, remainder 8 carry 1 = 8
#    9 + 9 + carry 1 = 19, remainder 9 carry 1 = 9
#    9 + 9 + carry 1 = 19, remainder 9 carry 1 = 9
#    9 + 9 + carry 1 = 19, remainder 9 carry 1 = 9
#    9 + 0 + carry 1 = 10, remainder 0 carry 1 = 0
#    9 + 0 + carry 1 = 10, remainder 0 carry 1 = 0
#    9 + 0 + carry 1 = 10, remainder 0 carry 1 = 0
#    0 + 0 + carry 1 = 1 , remainder 0 carry 0 = 1