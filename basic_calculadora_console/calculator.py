import os
import re
import time

#funções das operações
#soma
def sum(valor1,valor2):
    os.system('cls')    
    resultado = valor1 + valor2
    res_final =  f'O resultado da soma de {valor1} + {valor2} é: {resultado}'
    print(res_final)       
    time.sleep(5)   
    options() 
   

#subtração
def sub(valor1, valor2):
    os.system('cls')
    resultado = valor1 - valor2
    res_final = f'O resultado da soma de {valor1} - {valor2} é: {resultado}'
    print(res_final)
    time.sleep(5)
    options()

#divisão
def div(valor1, valor2):
    os.system('cls')
    resultado = valor1 / valor2
    res_final = f'O resultado da soma de {valor1} / {valor2} é: {resultado}'
    print(res_final)
    time.sleep(5)
    options()

#multiplicação
def mult(valor1, valor2):
    os.system('cls')
    resultado = valor1 * valor2
    res_final = f'O resultado da soma de {valor1} * {valor2} é: {resultado}'
    print(res_final)
    time.sleep(5)
    options()

#exit aplicação
def exit():
    os.system('cls')
    print('Deseja realmente sair da aplicação? S/N: ')
    user_response = input('Digite s ou n: ').lower()
    if user_response == 's':
        os._exit
        print('Saindo...')
        time.sleep(2)
        os.system('cls')
    else:
        options()



#opções
def options():
    os.system('cls')
    print('*******************************************************')
    print('************ Bem-vindo(a) basic calculator ************')
    print('*******************************************************')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4 - Multiplicação')
    print('0 - Sair')
    opcao_escolhida = int(input('digite a opção escolhida: '))
    match opcao_escolhida:
        case 1:   
            os.system('cls')  
            valor1 = int(input('digite o valor 1: '))       
            valor2 = int(input('digite o valor 2: '))
            sum(valor1, valor2)
        case 2:
            os.system('cls')
            valor1 = int(input('digite o valor 1: '))       
            valor2 = int(input('digite o valor 2: '))
            sub(valor1, valor2)
        case 3:
            os.system('cls')
            valor1 = int(input('digite o dividendo valor 1: '))       
            valor2 = int(input('digite o divisor valor 2: '))
            div(valor1, valor2)
        case 4:
            os.system('cls')
            valor1 = int(input('digite o multiplicando valor 1: '))       
            valor2 = int(input('digite o multiplicador valor 2: '))      
            mult(valor1, valor2)
        case 0:            
            exit()
            



#chamando aplicação
options()