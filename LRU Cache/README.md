[Back to Table of Contents](../README.md)

# LRU Cache
Difficulty: Medium

## Question
LRU Cache
Solved 
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in 
O
(
1
)
O(1) average time complexity.

Example 1:

Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)
Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000

## Solution Template
```python
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

        
```
