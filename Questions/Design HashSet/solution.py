class ListNode:

    def __init__(self, val):
        self.next = None
        self.val = val
        
class MyHashSet:
    def __init__(self):
        self.k = 10000
        self.arr = [ListNode(0) for _ in range(self.k)]

    def add(self, key: int) -> None:
        idx = key % self.k
        start = self.arr[idx]

        while start.next:
            if start.next.val == key:
                return
            start = start.next
        
        start.next = ListNode(val = key)


    def remove(self, key: int) -> None:
        idx = key % self.k
        start = self.arr[idx]

        while start.next:
            if start.next.val == key:
                start.next = start.next.next
                return
            start = start.next
        

    def contains(self, key: int) -> bool:
        idx = key % self.k
        start = self.arr[idx]

        while start.next:
            if start.next.val == key:
                return True
            start = start.next
        return False
    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)