from Cliente import Cliente
import pandas as pd

class adicionar_conta:
    def  __init__(self, nome_cliente, cpf_cliente, tipo_conta):#so e passado por parametro valores digitados pelos usuarios
        

        #criamos nossos molde da classe cliente para manipular  dados 
        self.cliente  = Cliente(nome_cliente, cpf_cliente, tipo_conta)#so e passado por parametro valores digitados pelos usuarios
    def adicionar(self, caminho_excel):
        nova_linha = len(caminho_excel) #visao da nova linha
        ultima_linha = caminho_excel.iloc[-1]

        dados_clientes = self.cliente.dicionario_cliente()

        dados_clientes["numero_conta"] = ultima_linha["numero_conta"]+1
        dados_clientes["agencia"] = ultima_linha["agencia"]+1

        novo_dado = pd.DataFrame(dados_clientes)
        return novo_dado



