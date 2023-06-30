from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        # Inicializa a capacidade máxima do cache
        self.capacity = capacity
        # Dicionário para armazenar os valores do cache
        self.cache = {}
        # Dicionário com as contagens de frequência de cada chave
        self.frequencies = defaultdict(int)
        # Frequência mínima atual
        self.min_frequency = 0

    def get(self, key):
        # Verifica se a chave está presente no cache
        if key in self.cache:
            # Obtém o valor e a frequência da chave do cache
            value, freq = self.cache[key]
            # Incrementa a frequência da chave
            self.frequencies[key] += 1
            # Atualiza a frequência mínima
            self.min_frequency = min(self.min_frequency, self.frequencies[key])
            # Retorna o valor associado à chave
            return value
        else:
            # Retorna None se a chave não estiver presente no cache
            return None

    def put(self, key, value):
        # Verifica se a capacidade do cache é zero (cache desabilitado)
        if self.capacity == 0:
            return

        # Verifica se a chave já está presente no cache
        if key in self.cache:
            # Obtém o valor e a frequência da chave do cache
            _, freq = self.cache[key]
            # Atualiza o valor e incrementa a frequência da chave
            self.cache[key] = (value, freq + 1)
            self.frequencies[key] += 1
            # Atualiza a frequência mínima
            self.min_frequency = min(self.min_frequency, self.frequencies[key])
            # Retorna o valor substituído, se houver
            return self.cache[key][0]
        else:
            # Verifica se o cache atingiu a capacidade máxima
            if len(self.cache) >= self.capacity:
                # Remove o item com a menor frequência
                self.remove_least_frequent()

            # Adiciona a chave e valor ao cache com frequência inicial 1
            self.cache[key] = (value, 1)
            self.frequencies[key] = 1
            # Define a frequência mínima como 1, pois a chave é nova
            self.min_frequency = 1

    def remove_least_frequent(self):
        # Lista para armazenar as chaves a serem removidas
        keys_to_remove = []
        # Itera sobre os itens do cache
        for key, (value, freq) in self.cache.items():
            # Verifica se a frequência é igual à frequência mínima
            if freq == self.min_frequency:
                # Adiciona a chave à lista de chaves a serem removidas
                keys_to_remove.append(key)

        # Remove as chaves do cache e das contagens de frequência
        for key in keys_to_remove:
            del self.cache[key]
            del self.frequencies[key]

        # Incrementa a frequência mínima após a remoção dos itens
        self.min_frequency += 1

    def clear(self):
        # Limpa o cache e as contagens de frequência
        self.cache.clear()
        self.frequencies.clear()
        self.min_frequency = 0

    def get_cache_state(self):
        # Retorna o estado atual do cache como uma lista de tuplas (chave, valor, frequência)
        state = []
        for key, (value, freq) in self.cache.items():
            state.append((key, value, freq))
        return state

# Exemplo de uso:
cache = LFUCache(3)
entries = [('A', 'Valor A'), ('B', 'Valor B'), ('B', 'Valor B'), ('C', 'Valor C'), ('D', 'Valor D'), ('E', 'Valor E')]
cache_operations = []

for key, value in entries:
    # Obtém o estado do cache antes da operação
    cache_state_before = cache.get_cache_state()
    # Realiza a operação de colocar (put) no cache e retorna o valor substituído, se houver
    replaced_value = cache.put(key, value)
    # Obtém o estado do cache após a operação
    cache_state_after = cache.get_cache_state()
    # Armazena a operação realizada e seus resultados em uma lista
    cache_operations.append((value, replaced_value, cache_state_before, cache_state_after))

for value, replaced_value, state_before, state_after in cache_operations:
    print("Valor da entrada:", value)
    if replaced_value is not None:
        print("Valor substituído:", replaced_value)
    print("Cache antes da entrada:", state_before)
    print("Cache depois da entrada:", state_after)
    print()

# Limpa o cache e imprime o estado vazio do cache
cache.cache.clear()
print("Cache vazia:", cache.get_cache_state())
