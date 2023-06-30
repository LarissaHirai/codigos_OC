from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end to indicate it was most recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if key in self.cache:
            # If the key already exists, move it to the end to indicate it was most recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # If the cache exceeds its capacity, remove the least recently used item
            self.cache.popitem(last=False)

# Example usage:
cache = LRUCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')

print(cache.get(1))  # Output: A
print(cache.get(2))  # Output: B
print(cache.get(4))  # Output: None

cache.put(4, 'D')
print(cache.get(3))  # Output: None (3 was the least recently used item, so it was removed from the cache)
