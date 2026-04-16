#Aqui estamos chamando nosso arquivo Cliente e a classe Cliente que esta dentro do arquivo Cliente
from Cliente import Cliente
from criar_conta import Criar_conta
from adicionar_conta import adicionar_conta #nome do arquivo primeiro e depois o nome da classe daquele arquivo
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

    df = pd.DataFrame()# criamos nosso data frame

    if os.path.exists(caminho_excel):
        print("Arquivo já existe")
        df = pd.read_excel(caminho_excel)

        #instanciando o adicionar conta
        adicionar = adicionar_conta(nome_cliente, cpf_cliente, tipo_conta,)#passamos por parametro somente os dados que serao digitados pelo usuario

        #chamando o funcao aidionar que esta dentro da classe Adicionar_conta
        novo_dado = adicionar.adicionar(df)

    else:
        print("Arquivo não existe")
        

        conta = Criar_conta(nome_cliente, cpf_cliente, tipo_conta) #instancia para manipular os dados adicionados pelo cliente

        novo_dado = conta.salvar_excel(caminho_excel)# identifico o caminho do excel e chama a funcao salvar_excel, ja com os dados ja prontos e com o return 

    df  = pd.concat([df, novo_dado], ignore_index  = True)#aqui recebemos o return o resultado do df = pd.DataFrame() e nosso dicionario que esta dados_clientes na criar_conta
    
    df.to_excel(caminho_excel, index = False)#salvamos o excel

    print(novo_dado)

elif escolha == 2:
    print("Opcao 2 selecionada")

#variaveis, paremetros e atributos 