from Cliente import Cliente
import pandas as pd

class adicionar_conta:
    def  __init__(self, nome_cliente, cpf_cliente, tipo_conta):
        numero_conta = 0
        agencia = 400
        extrato =0

        #criamos nossos molde da classe cliente para manipular  dados 
        self.cliente  = Cliente(nome_cliente, cpf_cliente, tipo_conta, numero_conta, agencia, extrato)
    def adicionar(self, caminho_excel):
        nova_linha = len(caminho_excel) #visao da nova linha
        ultima_linha = caminho_excel.iloc[-1]

        dados_clientes = {
        "nome_cliente" : [self.cliente.nome_cliente],
        "cpf_cliente" : [self.cliente.cpf_cliente],
        "tipo_conta" : [self.cliente.tipo_conta],
        "numero_conta": ultima_linha["numero_conta"] + 1, # aqui olhamos para ultima linha verificamos os dados composto nesta linha anterior e adicionamos mais 1 usando como base o dado anterior EX: era 400 aproxima fica 401
        "agencia" : ultima_linha["agencia"] + 1,
        "extrato_bancario" : [self.cliente.extrato],
        }

        novo_dado = pd.DataFrame(dados_clientes)
        return novo_dado



