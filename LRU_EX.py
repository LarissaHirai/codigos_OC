from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  # Cria um OrderedDict vazio para representar a cache

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move a chave acessada para o final do OrderedDict
            return self.cache[key]  # Retorna o valor correspondente à chave na cache
        else:
            return None  # Retorna None se a chave não está presente na cache

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move a chave já existente para o final do OrderedDict
        self.cache[key] = value  # Insere a chave-valor na cache
        if len(self.cache) > self.capacity:
            removed_key, removed_value = self.cache.popitem(last=False)  # Remove o item menos recente do início do OrderedDict
            print(f"Item removido: {removed_key}: {removed_value}")

    def clear(self):
        self.cache.clear()  # Limpa completamente a cache, removendo todos os itens

# Example usage with loop:
cache = LRUCache(3)  # Cria uma instância da classe LRUCache com capacidade máxima 3

inputs = [('A', 'Valor A'), ('B', 'Valor B'), ('C', 'Valor C'), ('D', 'Valor D'), ('E', 'Valor E')]
#[(1, 'A'), (2, 'B'), (3, 'C'), (1, 'X'), (4, 'D'), (2, 'Y')]  # Lista de entradas chave-valor

for key, value in inputs:
    print(f"Valor de entrada: {key}")
    print(f"Cache antes: {list(cache.cache.items())}")  # Exibe o estado atual da cache antes da operação
    result = cache.get(key)  # Obtém o valor correspondente à chave na cache
    if result is not None:
        print(result)  # Exibe o valor obtido, se não for None
    cache.put(key, value)  # Insere a chave-valor na cache
    print(f"Cache depois: {list(cache.cache.items())}")  # Exibe o estado atual da cache depois da operação
    print()

cache.clear()  # Limpa completamente a cache
print(f"Cache limpa: {list(cache.cache.items())}")  # Exibe a cache após ser limpa (deve estar vazia)
