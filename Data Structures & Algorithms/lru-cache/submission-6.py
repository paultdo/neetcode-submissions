
class Node:
    def __init__(self, key: int, value: int, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.move(key)
            return self.hash_map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        new = Node(key, value)
        if self.size == 0:
            self.head = new
            self.tail = self.head
        elif key in self.hash_map:
            if self.hash_map[key] == self.tail:
                self.tail = self.tail.prev
            elif self.head != self.hash_map[key]:
                self.hash_map[key].prev.next = self.hash_map[key].next
                self.hash_map[key].next.prev = self.hash_map[key].prev
            else:
                self.head = self.head.next
                self.head.prev = None

            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        
        if key in self.hash_map:
            del self.hash_map[key]
            self.size -= 1
        self.hash_map[key] = new
        self.size += 1
        if self.size > self.capacity:
            self.evict()

    def move(self, key:int) -> None:
        if self.tail != self.hash_map[key]:
            if self.head != self.hash_map[key]:
                self.hash_map[key].prev.next = self.hash_map[key].next
                self.hash_map[key].next.prev = self.hash_map[key].prev
            else:
                self.head = self.head.next
                self.head.prev = None
            self.hash_map[key].prev = self.tail
            self.tail.next = self.hash_map[key]
            self.tail = self.hash_map[key]
            self.tail.next = None

    def evict(self) -> None:
        if self.head:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None

            del self.hash_map[temp.key]

            self.size -= 1
        
