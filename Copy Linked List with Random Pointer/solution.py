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