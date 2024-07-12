#listas e alguns de seus métodos

#temos como estrutura de dados:
#listas
#tuplas
#sets
#dicionários

#listas serve para armazenar seus dados de uma forma sequencial
#cada posição possuem um indice para o elemento

#declarando uma lista
nomes = ['Fabricio', 'Melissa', 'Herbert', 'Rodrigo', 'Ana']
#temos o método append() -> adiciona um valor sequencialmente na lista ou seja na posição 0 em diante
nomes.append('José')
print(nomes)
#método index() -> passando o valor do elemento retorna a posição em que o elemento está
print(nomes.index('José'))
nomes.append('Bruno')
nomes.sort()
print(nomes)
#podemos misturar vários tipos de dados em uma lista... podemos adicionar outra lista, podemos adicionar dicionários etc
#outra forma de criar listas é já passar elementos na criação
carros = ['BMW i30', 'Ford Fusion', 'Astra', 'Celta', 'Corsa', 'Jeep Compass']
print(carros)
# o método append sempre adicionar o elemento no final da lista
#método insirt() -> precisa de dois parâmetros o primeiro é a posição desejada e o valor do elemento
carros.insert(1, 'Mercedez CLA')
print(carros)
#método para remover elementos da lista
#pop() -> remove sempre o último elemento da lista quando não é passado nenhum parâmetro
carros.pop()
print(carros)
#método del remove um elemento da lista -> passando o parâmetro do indice
del carros[1]
print(carros)
#método remove -> passando o valor do elemento para remover
carros.remove('Corsa')
print(carros)
#método count() -> pasando o valor do elemento ele retorna a quantidade de ocorrências que ele encontrar dentro da lista
print('quantidade de ocorrências:',carros.count('BMW i30'))
#método reverse() -> inverte a ordem da lista
carros.reverse()
print(carros)
#métodos sort() -> organiza os elementos em ordem alfanumérico
numeros = [4,3,2,1]
print(numeros)
numeros.sort()
print(numeros)