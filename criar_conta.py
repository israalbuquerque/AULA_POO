from Cliente import Cliente
import pandas as pd


class Criar_conta:
    def __init__(self, nome_cliente, cpf_cliente, tipo_conta):
        #aqui teremos nossos atributos
        numero_conta = 0
        agencia = 400
        extrato = 0

            #Instancia
        self.cliente  = Cliente(nome_cliente, cpf_cliente, tipo_conta, numero_conta, agencia, extrato)#O self aqui foi usado para definir como uma variavel que tera varios dados que pertence ao a variavel cliente
        #usamos o self para armazenar de forma prolongada os dados que estao sendo passados

    def salvar_excel(self, caminho_excel):
        dados_clientes = {
            "nome_cliente" : [self.cliente.nome_cliente],
            "cpf_cliente" : [self.cliente.cpf_cliente],
            "tipo_conta" : [self.cliente.tipo_conta],
            "numero_conta": [self.cliente.numero_conta],
            "agencia" : [self.cliente.agencia],
            "extrato_bancario" : [self.cliente.extrato],
        }

        excel = pd.DataFrame(dados_clientes)

        return excel