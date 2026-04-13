#Aqui estamos chamando nosso arquivo Cliente e a classe Cliente que esta dentro do arquivo Cliente
from Cliente import Cliente
from criar_conta import Criar_conta
import pandas as pd
import os

caminho_excel = "clientes_banco_Tabajara.xlsx"

print("**************** MENU ***************")

print("1- Criar conta")
print("2- Acessar conta")

print("**************************************")

escolha = int(input("Escolha uma das opções: "))

if escolha == 1:
    print("Opção 1 selecionada")
    nome_cliente = str(input("Digite seu nome completo: "))
    cpf_cliente = int(input("Digite seu cpf: "))
    tipo_conta = str(input("Digite o tipo da conta: "))

    if os.path.exists(caminho_excel):
        print("Arquivo já existe")
        df = pd.read_excel(caminho_excel)

    else:
        print("Arquivo não existe")
        df = pd.DataFrame()

        conta = Criar_conta(nome_cliente, cpf_cliente, tipo_conta) #instacio para manipular os dados adicionados pelo cliente

        novo_dado = conta.salvar_excel(caminho_excel)# identifico o caminho do excel e cahma a funcao salvar_excel
    
    df.to_excel(caminho_excel, index = False)

elif escolha == 2:
    print("Opcao 2 selecionada")

#variaveis, paremetros e atributos 