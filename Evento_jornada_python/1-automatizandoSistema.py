from operator import index
import pyautogui
import time
#pandas é a melhor lib para trabalhar com dados
#sempre bom instalar junto o openpyxl e o numpy
import pandas
#a cada comando do pyautogui o bot vai esperar o tempo setado
pyautogui.PAUSE = 0.6
#sistema
## https://dlp.hashtagtreinamentos.com/python/intensivao/login
#passo a passo
# passo 1 - entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(1.5)
# passo 2 - fazer login
pyautogui.click(x=846, y=388)
pyautogui.hotkey('ctrl','a')
pyautogui.write('romario@teste.com.br')
pyautogui.click(x=705, y=486)
pyautogui.hotkey('ctrl','a')
pyautogui.write('1234##@1212!@#$')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1.5)
# passo 3 - pegar/importar a base de dados
#para ler a base de dados utiliza-se o comando pandas.read() e a extensão do arquivo.
tabela = pandas.read_csv('.\Evento_jornada_python\produtos.csv')
# passo 4 - cadastrar um produto
#código
for linha in tabela.index:

    pyautogui.click(x=699, y=270)
    #o método loc localiza um item da tabela passando como parâmetro a linha e a coluna
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    #marca
    pyautogui.press('tab')
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    #tipo
    pyautogui.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    #categoria
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    #preço unitário
    pyautogui.press('tab')
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write('custo')
    #custo
    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    #obs
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    #enviar    
    pyautogui.press('tab')
    pyautogui.press('enter')    
    pyautogui.press('home')
    time.sleep(0.5)
    # passo 5 - repetir o passo 4 até cadastrar todos os produtos


#aulas complementares
#Como Transformar Arquivo Python em Executável - [Arquivo Executável]
#Executar Código em Python Automaticamente (Diariamente, Semanalmente)

#39894