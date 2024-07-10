# Objetos possuem propriedades como: marca, modelo, cor, tipo de bateria etc…
# Objetos possuem funções como: fazer ligações, jogos, relógio, alarmes etc…
# exemplo de como declarar uma classe de objeto
# class Pessoa:
# nome = ‘Romário’
# idade = ‘30’
# RG = ‘43.345.543-5’
# CPF = ‘320.543.453-90’
# naturalidade = ‘São Paulo’
# def trabalhar(self):
# print(’trabalhando…’)
# def pagar_boletos(self):
# print(’pagando boletos’)
# def dormir(self):
# print(’dormindo’)
# Toda função dentro de uma classe precisa ter o parâmetro self, pois ele refere-se ao objeto em si.
# método construtor
# def __ init __ (self, propriedades):
# self.propriedade = propriedade
# instanciando
# objeto = Objeto(propriedades)

#declarando objeto
class Carro():
    #método construtor
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

#declarando dicionário vazio
carros = {}

#pegando input do usuário
marca = input('informe a marca: ')
modelo = input('informe o modelo: ')
ano = int(input('informe o ano: '))
preco = int(input('informe o preço: '))

#instanciando o objeto
carro = Carro(marca, modelo, ano, preco)

#adicionando carro ao dicionário utilizando marca como chave
carros[carro.marca] = carro

#for para exibir informações dos carros na lista
for marca, carro in carros.items():
    n = 1
    print(f'{n} - Marca:{carro.marca} | Modelo:{carro.modelo} | Ano:{carro.ano} | Preço:{carro.preco}')
    n = n + 1