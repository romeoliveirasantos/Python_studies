from multiprocessing import Value
from optparse import Values
import pandas as pd

data = pd.read_excel('Automa_info\data\VendaCarros.xlsx')
# print(type(data))

#1 - selecionando colunas específicas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

#2 - criando a tabela pivô
pivot_table = df.pivot_table(
    index = "Ano",
    columns = "Fabricante",
    values = "ValorVenda",
    aggfunc = "sum"    
)

#3 - exportando tabela pivô em arquivo excel
pivot_table.to_excel('Automa_info\data\pivot_table.xlsx', 'Relatorio')