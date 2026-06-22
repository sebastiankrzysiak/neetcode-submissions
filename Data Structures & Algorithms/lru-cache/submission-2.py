class Node:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.left = Node()
        self.right = Node()
        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        
        node = self.hashMap[key]
        val = node.val
        self.remove(node)
        del self.hashMap[key]
        self.put(key, val)

        return val   

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)
            del self.hashMap[key]

        self.hashMap[key] = Node(key, value)
        rightPrev = self.right.prev
        rightPrev.nxt = self.hashMap[key]
        self.hashMap[key].prev = rightPrev
        self.right.prev = self.hashMap[key]
        self.hashMap[key].nxt = self.right

        if len(self.hashMap) > self.capacity:
            lru_node = self.left.nxt
            self.remove(lru_node)
            del self.hashMap[lru_node.key]