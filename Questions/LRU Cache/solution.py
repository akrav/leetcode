class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.nex = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.left = Node(0, 0) #pointer to least recently used 
        self.right = Node(0, 0) #pointer of most recently used
        self.left.nex = self.right #point pointers to eachother
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev # get nodes prev
        nex = node.nex # get nodes next
        prev.nex = nex # connect prev to the node's next skipping the node
        nex.prev = prev # connect nex to the node's prev skipping the node


    
    def insert(self, node):
        prev = self.right.prev #old most recently used
        nex = self.right # most recently used pointer identifier
        prev.nex = node  # old most recently used points to new recently used point
        nex.prev = node  # most recently used pointer identifier points back to new node for recently used 
        node.nex = nex   # make new most recently used node point to most recently used pointer identifier
        node.prev = prev # make new most recently used node point prev to old most recently used node

    def get(self, key: int) -> int:
        if key in self.dic.keys():
            self.remove(self.dic[key])
            self.insert(self.dic[key])
            return self.dic[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic.keys():
            self.remove(self.dic[key])
        self.dic[key] = Node(key, value)
        self.insert(self.dic[key])

        if len(self.dic) > self.capacity:
            lru = self.left.nex
            self.remove(lru)
            self.dic.pop(lru.key)

        