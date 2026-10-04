class CacheNode:
    def __init__(self, key: Optional[int] = None, value: int = -1, previous: CacheNode = None, next: CacheNode = None):
        self.value = value
        self.previous = previous
        self.next = next
        self.key = key
    
    # def set_previous(self, new_previous: CacheNode) -> None:
    #     if self.previous == new_previous:
    #         return
    #     previous = self.previous
    #     self.previous = new_previous
    #     new_previous.next = self
    #     previous.next = new_previous
    #     new_previous.previous = previous
    
    def set_next(self, new_next: CacheNode) -> None:
        if self.next == new_next:
            return
        next = self.next
        self.next = new_next
        new_next.previous = self
        next.previous = new_next
        new_next.next = next

    def self_remove(self) -> None:
        self.previous.next = self.next
        self.next.previous = self.previous
        self.next = None
        self.previous = None


class LRUCache:

    def __init__(self, capacity: int):
        self.most_recent = CacheNode()
        self.least_recent = CacheNode
        self.most_recent.next = self.least_recent
        self.least_recent.previous = self.most_recent
        self.map = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if not key in self.map:
            return -1
        
        node = self.map[key]
        node.self_remove()
        self.most_recent.set_next(node)
        return self.map[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.self_remove()

        new_node = CacheNode(key, value)
        self.map[key] = new_node
        self.most_recent.set_next(new_node)

        if len(self.map) == self.capacity + 1:
            node = self.least_recent.previous
            node.self_remove()
            del self.map[node.key]
        
