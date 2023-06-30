import random

class RandomCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if self.capacity == 0:
            return

        if len(self.cache) >= self.capacity:
            # Se a cache está cheia, remove um item aleatório
            random_key = random.choice(list(self.cache.keys()))
            del self.cache[random_key]

        self.cache[key] = value

# Exemplo de uso:
cache = RandomCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')

print(cache.get(1))  # Output: A
print(cache.get(2))  # Output: B
print(cache.get(4))  # Output: None

cache.put(4, 'D')
print(cache.get(3))  # Output: None (um item aleatório foi removido da cache)
