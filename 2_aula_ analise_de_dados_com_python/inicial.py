#passo a passo
#libs: pandas openpyxl numpy ipykernel nbformat plotly
#para trabalhar com dados melhor lib é pandas
#para trabalhar com gráficos melhor lib é plotly
import pandas as pd
#passo 1: importar a base de dados
tabela = pd.read_csv('2_aula_ analise_de_dados_com_python\cancelamentos_sample.csv')
#display exibe a base graficamente melhor e só é permitido em arquivos do tipo ipynb
#passo 2: Visualizar a base de dados
          #entender o que tem na base de dados
          #encontrar os erros na base de dados
            #coulunas inúteis - informação que não te ajuda, te atrapalha
            #tirar coluna de CustomerID
tabela = tabela.drop(columns='CustomerID') #drop exclui colunas ou linhas pode excluir mais de uma utilizando ['nome da coluna']

print(tabela)

#passo 3:Tratamento de dados - corrigir erros da base
            #informações no formato errado
print(tabela.info())
            #valores vazios
#excluindo valores vazios da tabela
tabela = tabela.dropna() #metodo fillna() preenche valores vazios passando parâmetro

#passo 4: Análise inical dos cancelamentos
#selecionar uma coluna específica da tabela
#exibir o count da coluna com base na coluna cancelou
print(tabela['cancelou'].value_counts())
#para exibir esse count em porcentagem utiliza-se normalize=True como parâmetro
#print(tabela['cancelou'].value_counts(normalize=True).map('{:.2%}'.format)) 
#.map() formata com base em código como parâmetro do método {:1%}.format o .1 é as casas decimais
#passo 5: Análise de causa do cancelamento do cliente
#plotly seaborn ou matplotlib são opções para criar gráficos
import plotly.express as px
#criar gráfico com for para iterar sobre as colunas da tabela, para cada coluna irá criar um gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='cancelou') #color exibe cores diferentes com base na coluna cancelou
    #exibir gráfico
    grafico.show()

#todos os clientes que ligaram mais de 4x pro call center, cancelaram
    #criar um processo interno para resolver os problemas do cliente no máximo em 2 ou 3 ligações
#todos os clientes que atrasaram mais de 20 dias o pagamento, cancelou
    #criar um alerta para quando bater 10 dias, alertar o time de suporte para contatar o cliente
#todos os clientes de contrato mensal cancelaram
    #oferecer desconto no contrato anual/trimestral

#resolver o call center, pra quanto cai o cancelamento?
filtro = tabela['ligacoes_callcenter'] <= 4
tabela = tabela[filtro]
print(tabela['cancelou'].value_counts(normalize=True))
#resolver o atraso, para quanto cai o cancelamento?
filtro = tabela['dias_atraso'] <= 20
tabela = tabela[filtro]
#resolver o contrato mensal, para quanto cai o cancelamento?
filtro = tabela['duracao_contrato'] != 'Monthly'
tabela = tabela[filtro]

print(tabela['cancelou'].value_counts(normalize=True))