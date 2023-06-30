from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequencies = defaultdict(int)
        self.min_frequency = 0

    def get(self, key):
        if key in self.cache:
            value, freq = self.cache[key]
            # Atualiza a frequência do item e a frequência mínima se necessário
            self.frequencies[key] += 1
            self.min_frequency = min(self.min_frequency, self.frequencies[key])
            return value
        else:
            return None

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            # Se a chave já existe na cache, atualiza o valor e aumenta a frequência
            _, freq = self.cache[key]
            self.cache[key] = (value, freq + 1)
            self.frequencies[key] += 1
            self.min_frequency = min(self.min_frequency, self.frequencies[key])
        else:
            if len(self.cache) >= self.capacity:
                # Se a cache está cheia, remove o item menos frequentemente usado
                self.remove_least_frequent()

            # Insere o novo item na cache com frequência 1
            self.cache[key] = (value, 1)
            self.frequencies[key] = 1
            self.min_frequency = 1

    def remove_least_frequent(self):
        keys_to_remove = []
        for key, (value, freq) in self.cache.items():
            if freq == self.min_frequency:
                keys_to_remove.append(key)

        for key in keys_to_remove:
            del self.cache[key]
            del self.frequencies[key]

        self.min_frequency += 1

# Exemplo de uso:
cache = LFUCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')

print(cache.get(1))  # Output: A
print(cache.get(2))  # Output: B
print(cache.get(4))  # Output: None

cache.put(4, 'D')
print(cache.get(3))  # Output: None (3 foi o menos frequentemente usado, então foi removido da cache)
