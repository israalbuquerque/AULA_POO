import pandas as pd
from Cliente import Cliente

class Acessar_conta:
    def __init__(self,cpf_cliente ,numero_conta):
        self.cliente = Cliente(nome_cliente="", cpf_cliente = cpf_cliente, tipo_conta =0 ,numero_conta = 0, agencia = 400, extrato = 0 )

    def validar_banco(self, caminho_excel):#nosso metodo
        df = pd.read_excel(caminho_excel)

        cliente_encontrado = df[
            (df["cpf_cliente"].astype(str) == str(self.cliente.cpf_cliente)) & 
            (df["numero_conta"].astype(str )== str(self.cliente.numero_conta))
        ]

        #se o cliente for encontrado entao mostrar a mensagem bem vindo e trazer os dados solicitados

        if not cliente_encontrado.empty:#empty significa vazio e temos um not(entao lemos, cliente_encontrado nao estiver vazio entao)
            nome = cliente_encontrado.iloc[0]["nome_cliente"]
            print(f"Olá {nome} bem - vindo ao banco Tabajara")
            return True
            
        else:
            print("Usuário não encontrado, tentar novamente ou realizar cadastro")
            return False