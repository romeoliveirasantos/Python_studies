from openpyxl import load_workbook

#1 - Lê pasta de trabalho e planilha
#importando workbook
wb = load_workbook('Automa_info\data\pivot_table.xlsx')
#acessando a planilha relatório
sheet= wb['Relatorio']
#acessando um valor específico
#print(sheet['A3'].value)
#print(sheet['B3'].value)

#2 - Iterando valores por meio de loop
for i in range(2,6):
    ano = sheet['A%s' %i].value
    am = sheet['B%s' %i].value
    bt = sheet['C%s' %i].value
    #format é tipo uma string literals ou template string
    print('{0} o Aston martin vendeu {1} e o Bentley vendeu {2}'.format(ano,am,bt))