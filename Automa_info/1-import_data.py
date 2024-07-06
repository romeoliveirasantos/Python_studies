#voce pode dar um apelidado 'alias' para a biblioteca só precisa utilizar 'as *apelido* '
import pandas as pd

# 1 - importando dados
data = pd.read_excel('Automa_info\data\VendaCarros.xlsx')
print(data)
# 2 - Lista os primeiros registros
# você pode passar no parâmetro do método quantos registros quer mostrar
print(data.head())
# 3 - tail mostra os últimos registros
print(data.tail())
# 4 - contagem de valores por fabricante (dentro do colchetes você pode por a coluna desejada)
#value_counts tras a contagem por fabricante
print(data['Fabricante'].value_counts())

