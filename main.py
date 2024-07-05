variaveis com input e convert
nome = input("Digite seu nome:")
idade = int(input("Digite seu nome:"))
peso = float(input("Digite seu nome:"))

print(type(nome), nome)
print(idade)
print(peso)

#operadores
soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30/3
potencia = 7 ** 2

print(soma)
print(multiplicacao)
print(divisao, 'Tipo: ', type(divisao))
print(potencia)

idade = int(input('Informe sua idade: '))

if idade >= 18:
    print('Permitido')
else:
    print('Bloqueado')

salario = float(input('Informe o salário'))

#condicionais
if salario <= 3000:
    print('Programador Junior')
elif salario > 3000 and salario <= 6000:
    print('Programador Pleno')
elif salario > 6000 and salario <= 15000:
    print('Programador senior')
else:
    print('Gerente de projetos') 

listas - arrays
listas são conjuntos de dados armazenados em variável
from audioop import reverse
from operator import truediv
from turtle import circle


list_numeros = [1,2,3]
list_numeros[1] = 4 
print('Primeiro item:',list_numeros[0])
print('Segundo item:',list_numeros[1])
print('Terceiro item:',list_numeros[2])

metodo append - adicionar
outros métodos
insert [posição,item]- insere um ovo item a posição dada
pop - remove e retorna o ultimo item
pop [posição] - remove e retorna o item da posição
sort - ordena a lista
reverse - ordena a lista em ordem reversa
index [item] - retorna a posição da primeira ocorrência do item
count [item] - retorna o número de ocorrências do item
remove [item] - remove a primeira ocorrência do item
lista_vazia = []

lista_vazia.append('Romário')
lista_vazia.append('Victor')
lista_vazia.reverse()
listOrdenada = [1,2,3,4]
listOrdenada.reverse()
print(listOrdenada)
listOrdenada.sort()
print(listOrdenada)
print(lista_vazia)
lista_vazia.pop()
print(lista_vazia)

len(lista) retorna o tamanho da lista
min(lista) retorna o menor valor da lista
max(lista) retorna o maior da lista
print(len(listOrdenada))
listOrdenada.pop(1)
print(len(listOrdenada))
print(max(listOrdenada))
print(min(listOrdenada))

repetições - loop
for repete com um número de repetições definida
while repete enquanto uma condição for verdadeira

exemplo de for com o parametro range
lista vazia
notas = []

#for para registrar as notas dos alunos
for x in range(5):
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    #populando uma lista de resultados
    resultado = [codigo_aluno, nota]
    #inserindo o resultado na lista de notas
    notas.append(resultado)

print('Quantidade de notas', len(notas))

#for para exibir as notas dos alunos
    for n in notas:
        codigo_aluno = n[0]
        nota = n[1]
        print('O RM', codigo_aluno, 'Tirou a nota: ', nota)

exemplo com while
notas = []
contador = 1

while contador <= 5:
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    contador = contador + 1


print('Quantidade de notas', len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print('O aluno', codigo_aluno, 'tirou a nota: ', nota)

dicionários - objetos
dicionários são estruturas que armazenam chaves e valores
a chave e valores são chamados de atributos dentro do dicionário
exemplo de dicionário
pessoa = {
    "nome" : "Romário",
    "idade": 30,
    "cidade": "São paulo"
}
#exemplo de como acessar os atributos
print('Nome:', pessoa["nome"], '-', pessoa["idade"], 'anos', 'cidade:', pessoa["cidade"])

#exemplo de lista de dicionários
player = {
    'nick' : "Roxohq",
    'level' : 15,
    'hp' : 150,
    'exp': 1300,
    "dano" : 45
}
#lista de dicionário de BOSSES
bosses = [
    {'nome':'Mardukie', 'dano':20, 'hp': 150, 'exp':300, 'tipo': 'fogo' },
    {'nome':'Glacier', 'dano':60, 'hp': 450, 'exp':500, 'tipo': 'gelo' },
    {'nome':'Khartuz', 'dano':80, 'hp': 650, 'exp':700, 'tipo': 'morte' }
]
exibindo os dados dos bosses, como cada elemento b já é um dicionário dentro da lista, basta acessar os valores
for b in bosses:
    nome = b['nome']
    dano = b['dano']
    elemento = b['tipo']
    print('Boss:', nome, 'Dano:', dano, 'Elemento', elemento)






criando um chat de menssagens para praticar
no python podemos importar script(bibliotécas)
import os

#lista de mensagens vazia
mensagens = []

#nome do usuário
nome = input('Nome: ')

#looping
while True:
    #limpando terminal
    #windonws comando 'cls' limpa o terminal, linux 'clear'
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])

    print('-----------------------------')

    #obtendo o texto
    texto = input('Mensagem: ')
    if texto == 'fim':
        #o break encerra o looping
        break

    #adicionando mensagens na lista
    mensagens.append({
        'nome': nome,
        'texto': texto
    })


funções
funções são blocos de códigos reutilizaveis que realizam tarefas específicas
exemplo de função
import os
import time

def minha_primeira_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    os.system('cls')
    valor1 = int(input('Valor1: '))
    valor2 = int(input('Valor2: '))
    resposta = minha_primeira_funcao(valor1,valor2)
    print(valor1, '+', valor2, '=', resposta)
    print('Aguarde 3 segundos, reiniciando!')
    time.sleep(3)



