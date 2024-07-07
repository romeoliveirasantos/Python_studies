alunos = []

nome = input('informe o nome do aluno: ')
serie = input('informe a serie do aluno: ')

def add_alunos(nome,serie):
    count = 1
    aluno = {
        'id' : count,
        'nome': nome, 
        'serie': serie
    }
    alunos.append(aluno)

add_alunos(nome,serie)

def exibe_aluno():
    for aluno in alunos:
        print(f'id: {aluno['id']} - Nome: {aluno['nome']} - Série: {aluno['serie']}')
        

exibe_aluno()


def insere_fruta():
    frutas = []
    fruta = input('qual é a fruta? ')    
    quantidade = int(input('qual a quantidade? '))
    resultado = f'{fruta} - {quantidade}'
    frutas.append(resultado)    
    for fruta in frutas:
        print(f'Fruta: {fruta}x')


insere_fruta()