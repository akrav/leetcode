class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.k = 10000
        self.arr = [ListNode(None) for i in range(self.k)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.k
        curr = self.arr[idx]

        while curr.next:
            if curr.next.val is not None and curr.next.val[0] == key:
                curr.next.val = [key, value]
                return
            curr = curr.next
        curr.next = ListNode([key, value])

        

    def get(self, key: int) -> int:
        idx = key % self.k
        curr = self.arr[idx]

        while curr.next:
            if curr.next.val is not None and curr.next.val[0] == key:
                return curr.next.val[1]
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = key % self.k
        curr = self.arr[idx]

        while curr.next:
            if curr.next.val is not None and curr.next.val[0] == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)