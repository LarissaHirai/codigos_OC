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

        if len(self.cache) >= self.capacity:
            oldest = self.cache.popleft()
            print("Substituído:", oldest[0], "=", oldest[1])

        self.cache.append((key, value))
        print("Entrada:", (key, value))
        print("Cache antes da entrada:", self)
        print("Cache depois da entrada:", self)

    def __str__(self):
        items = [str(item[0]) for item in self.cache]
        return "[" + ", ".join(items) + "]"

cache = FIFOCache(3)

inputs = [('A', 'Valor A'), ('B', 'Valor B'), ('C', 'Valor C'), ('D', 'Valor D'), ('E', 'Valor E')]

for key, value in inputs:
    cache.put(key, value)
    print("Valores substituídos:", cache.cache)
    print()

print("Entradas na cache:")
for key, value in inputs:
    cache_value = cache.get(key)
    print("Entrada:", (key, value))
    print("Valor da cache:", cache_value)
    print()

cache.cache.clear()

print("Cache vazia:", cache)
