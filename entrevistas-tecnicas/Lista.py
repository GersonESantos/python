
# Exemplo de operações eficientes com listas (vetores) em Python

# Criação da lista
lista = list(range(1, 10))
print('Lista inicial:', lista)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Acesso eficiente por índice
print('Primeiro elemento:', lista[0])      # 1
print('Segundo elemento:', lista[1])       # 2
print('Último elemento:', lista[-1])       # 9

# Adicionando elemento ao final
lista.append(10)
print('Após append(10):', lista)           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Removendo último elemento (pop)
removido = lista.pop()
print('Elemento removido com pop():', removido)  # 10
print('Após pop():', lista)                      # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obtendo tamanho da lista
print('Tamanho da lista:', len(lista))           # 9

# Alterando elemento por índice
lista[1] = -1
print('Após alteração do segundo elemento:', lista)  # [1, -1, 3, 4, 5, 6, 7, 8, 9]
