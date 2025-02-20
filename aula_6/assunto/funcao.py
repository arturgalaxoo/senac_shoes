# SINTAXE BÁSICA DE UMA FUNÇÃO 

def nome_da_funcao(parametros):
     # codigo da função
     resultado = 0
     return resultado

def ola_mundo():
    print("Olá Mundo.")

ola_mundo() # Chamando a função (invocando a função)

# Função com retorno e com parâmetros
def saudacao(nome):
    print(f'Olá, seja bem-vindo(a) {nome}')

saudacao("Artur")
saudacao("Leticia")

# Função com parâmetros e retorno
def somar(numero1, numero2):
    soma = numero1 + numero2
    return soma

print(somar(10,20))