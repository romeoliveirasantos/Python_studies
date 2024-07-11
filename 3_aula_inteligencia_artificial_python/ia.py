# Projeto Python IA: Inteligência Artificial e Previsões
### Case: Score de Crédito dos Clientes
# Você foi contratado por um banco para conseguir definir o score de crédito dos clientes. 
# Você precisa analisar todos os clientes do banco e, com base nessa análise, criar um modelo que consiga ler as informações do cliente
# e dizer automaticamente o score de crédito dele: Ruim, Ok, Bom
# Arquivos da aula: https://drive.google.com/drive/folders/1FbDqVq4XLvU85VBlVIMJ73p9oOu6u2-J?usp=drive_link
#como criar IA - projeto de previsão

#libs: pandas para trabalhar com dados e sciit-learn para trabalhar com IA
#passo a passo
#passo 0 - entender o desafio da empresa e da sua área
#passo 1 - importar base de dados
import pandas as pd
tabela = pd.read_csv('3_aula_inteligencia_artificial_python\clientes.csv')
print(tabela)
#verificar se a base tem problemas
print(tabela.info())
#float -> números com casa decimal
#int -> números inteiros
#object -> texto
#passo 2 - preparar a base de dados para inteligência artificial
#pre processing
#tratar textos -> IA só pode aprender com números
#colunas de texto: 
#label encoder -> codificar com rótulo
# profissao
from sklearn.preprocessing import LabelEncoder
codificador = LabelEncoder()
tabela['profissao'] = codificador.fit_transform(tabela['profissao'])
# mix_credito 
tabela['mix_credito'] = codificador.fit_transform(tabela['mix_credito'])
# comportamento_pagamento
tabela['comportamento_pagamento'] = codificador.fit_transform(tabela['comportamento_pagamento'])
print(tabela.info())
#x é quem a IA pode usar para fazer a previsão
#y é quem a IA tem que prever
x = tabela.drop(columns=['score_credito', 'id_cliente']) 
y = tabela['score_credito']
       
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)
#passo 3 - criar um modelo de IA -> nota de crédito: Ruim, média ou boa
#arvore de decisão -> randomForest
#neirest neigbors -> KNN -> vizinhos próximos

#3 etapas para criar a IA

#importar a IA
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


#criar a IA
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

#treinar IA
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)
#passo 4 - escolher melhor modelo
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_teste, previsao_arvoredecisao))
print(accuracy_score(y_teste, previsao_knn))

#passo 5 - usar modelo escolhido para fazer novas previsões
# o modelo dda arvore de decisao é o melhor modelo

#nova previsão
#importar novos clientes
tabela_novos_clientes = pd.read_csv('novos_clientes.csv')

#tratar dados da tabela -> colunas de texto
from sklearn.preprocessing import LabelEncoder
codificador = LabelEncoder()
tabela_novos_clientes['profissao'] = codificador.fit_transform(tabela_novos_clientes['profissao'])
# mix_credito 
tabela_novos_clientes['mix_credito'] = codificador.fit_transform(tabela_novos_clientes['mix_credito'])
# comportamento_pagamento
tabela_novos_clientes['comportamento_pagamento'] = codificador.fit_transform(tabela_novos_clientes['comportamento_pagamento'])
print(tabela_novos_clientes)
#fazer previsões -> modelo_arvoredecisao
previsoes = modelo_arvoredecisao.predict(tabela_novos_clientes)
print(previsoes)



