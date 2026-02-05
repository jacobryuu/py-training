from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def put(self, key: str, value: int):
        """Add or update a key-value pair in the cache"""
        if key not in self.cache and len(self.cache) >= self.capacity:
            # Remove oldest item (first item)
            self.cache.popitem(last=False)
        self.cache[key] = value
        # Move to end to mark as recently used
        self.cache.move_to_end(key)
    
    def get(self, key: str) -> int:
        """Get value for a key, returns -1 if not found"""
        if key not in self.cache:
            return -1
        # Move to end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]


def main():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    print(cache.get("a"))  # 1
    cache.put("c", 3)  # evicts "b"
    print(cache.get("b"))  # -1
    print(cache.get("c"))  # 3


if __name__ == "__main__":
    main()
