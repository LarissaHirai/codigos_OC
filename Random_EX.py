import random

class RandomCache:
    def __init__(self, capacity):
        # Inicializa a classe RandomCache com a capacidade máxima definida
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        # Retorna o valor associado à chave, se existir na cache, caso contrário retorna None
        if key in self.cache:
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        replaced_value = None
        if len(self.cache) >= self.capacity:
            # Remove um item aleatório da cache e armazena o valor substituído
            random_key = random.choice(list(self.cache.keys()))
            replaced_value = self.cache.pop(random_key)
        # Adiciona o novo par chave-valor à cache
        self.cache[key] = value
        return replaced_value

    def clear(self):
        # Limpa a cache, removendo todos os pares chave-valor
        self.cache.clear()

    def get_cache_state(self):
        # Retorna uma cópia do estado atual da cache
        return self.cache.copy()

# Exemplo de uso:
cache = RandomCache(3)
entries = [('A', 'Valor A'), ('B', 'Valor B'), ('C', 'Valor C'), ('D', 'Valor D'), ('E', 'Valor E')]

cache_operations = []

for key, value in entries:
    cache_state_before = cache.get_cache_state()
    replaced_value = cache.put(key, value)
    cache_state_after = cache.get_cache_state()
    cache_operations.append((value, cache_state_before, cache_state_after, replaced_value))

for value, state_before, state_after, replaced_value in cache_operations:
    print("Valor da entrada:", value)
    print("Cache antes da entrada:", state_before)
    print("Cache depois da entrada:", state_after)
    if replaced_value is not None:
        print("Valor substituído:", replaced_value)
    print()

# Limpa a cache
cache.cache.clear()

# Imprime a cache vazia
print("Cache vazia:", cache.get_cache_state())
