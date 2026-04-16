import pandas as pd
from Cliente import Cliente

class Acessar_conta:
    def __init__(self, cpf_cliente, numero_conta):
        self.cliente = Cliente(cpf_cliente, numero_conta, tipo_conta="")

    def validar_banco(self, caminho_excel):#nosso metodo
        df = pd.read_excel(caminho_excel)

        cliente_encontrado = df[
            (df["cpf_cliente"] == self.cliente.cpf_cliente) & 
            (df["numero_conta"]== self.cliente.numero_conta)
        ]

        #se o cliente for encontrado entao mostrar a mensagem bem vindo e trazer os dados solicitados

        if not cliente_encontrado.empty:#empty significa vazio e temos um not(entao lemos, cliente_encontrado nao estiver vazio entao)
            print("Bem - vindo ""ao banco Tabajara")
        else:
            print("Usuário não encontrado, tentar novamente ou realizar cadastro")