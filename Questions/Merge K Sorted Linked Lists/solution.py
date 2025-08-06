# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# #First attempt logic
# import heapq as hq
# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         pq = []
#         for li in lists:
#             while li:
#                 hq.heappush(pq, li.val)
#                 li = li.next
        
#         head = ListNode()
#         dummy = head
#         for i in range(len(pq)):
#             val = hq.heappop(pq)
#             new_node = ListNode(val)
#             head.next = new_node
#             head = head.next
        
#         return dummy.next

# #second attempt logic after looking at the solution
# import heapq as hq
# class NodeWrapper:
#     def __init__(self, node):
#         self.node = node
#     # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
#     # Heap uses < operator so we need to write the "dunder" function for less than which is below
#     # __eq__(self, other): Defines equality (==).
#     # __ne__(self, other): Defines “not equal” (!=).
#     # __lt__(self, other): Less than (<).
#     # __le__(self, other): Less than or equal (<=).
#     # __gt__(self, other): Greater than (>).
#     # __ge__(self, other): Greater or equal (>=).
#     def __lt__(self, other):
#         #heap is comparing NodeWrappers since that is what is being stored
#         return self.node.val < other.node.val

# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         pq = []
#         for li in lists:
#             while li:
#                 hq.heappush(pq, NodeWrapper(li))
#                 li = li.next
        
#         head = ListNode()
#         dummy = head
#         for i in range(len(pq)):
#             new_node = hq.heappop(pq).node #popping off node wrapper thus convert to node
#             head.next = new_node
#             head = head.next
        
#         return dummy.next

        



#third attempt logic after looking at the solution
import heapq as hq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                new_list = self.mergeLists(l1, l2)
                merged_lists.append(new_list)
            lists = merged_lists
        return lists[0]
    
    def mergeLists(self, l1, l2):
        head = ListNode()
        dummy = head
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        if l1:
            head.next = l1

        if l2:
            head.next = l2
        
        return dummy.next