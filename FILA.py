from collections import deque

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = deque()

    def get(self, key):
        for item in self.cache:
            if item[0] == key:
                return item[1]
        return None

    def put(self, key, value):
        if self.capacity == 0:
            return

        # Remove the oldest item if the cache is full
        if len(self.cache) >= self.capacity:
            self.cache.popleft()

        # Insert the new item at the end of the queue
        self.cache.append((key, value))

# Example usage:
cache = FIFOCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')

print(cache.get(1))  # Output: A
print(cache.get(2))  # Output: B
print(cache.get(4))  # Output: None

cache.put(4, 'D')
print(cache.get(3))  # Output: None (3 was the oldest item, so it was removed from the cache)
