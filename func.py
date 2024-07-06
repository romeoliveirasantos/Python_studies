#praticando funções - manipulação de lista e dicionário

import os
import time


#lista para armazenar o nome e o setor do funcionário cadastrado
colaboradores = []


def menu_opcoes():
    os.system('cls')
    print('Registrador de funcionários')
    print('____________________________')
    print('0 - sair')
    print('1 - registrar novo funcionário')
    print('2 - remover registro de funcionário')
    print('3 - exibir lista de funcionários registrados')
    opcao = int(input('Digite a opção desejada: '))
    opcoes(opcao)

def exit():
    os.system('cls')
    sair = input('tem certeza que deseja sair S/N: ')        
    if sair.lower() == 's':
        print('saindo...')
        time.sleep(3)
        os._exit
    else:
        print('retornando para o menu principal')
        time.sleep(3)
        menu_opcoes()

def reg_colab():    
    os.system('cls' if os.name == 'nt' else 'clear')
    registrar = True
    while registrar:
            funcionario = {}
            funcionario['nome'] = input('informe o nome do funcionário: ')           
            funcionario['setor'] = input('informe o setor do funcionário: ')
            funcionario['salário'] = input('informe o salário do funcionário: ')
            colaboradores.append(funcionario)
            continuar = input('deseja registrar mais um funcionário? s/n: ')
            if continuar.lower() == 'n':
                registrar = False
                menu_opcoes()
            else:
                registrar = True
                os.system('cls' if os.name == 'nt' else 'clear')

def remove_colab():
    nome = input('Informe o nome do funcionário a ser removido: ')
    encontrado = False
    for funcionario in colaboradores:
        if funcionario['nome'].lower() == nome.lower():
            colaboradores.remove(funcionario)
            print(f'Funcionário {nome} removido com sucesso.') 
            encontrado = True
            time.sleep(3)
            menu_opcoes()
        if not encontrado:
            print(f'Funcionário {nome} não encontrado')

def show_colab():
    for funcionario in colaboradores:
      print(f"Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: {funcionario['salário']}")
      
      
    time.sleep(3)  
    menu_opcoes()

def opcoes(opcoes):

    match opcoes:
        case 1:             
            reg_colab()
        case 2:            
            remove_colab()
        case 3:            
            show_colab()
        case 0:            
            exit()



menu_opcoes()