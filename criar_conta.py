from Cliente import Cliente
import pandas as pd


class Criar_conta:
    def __init__(self, nome_cliente, cpf_cliente, tipo_conta):#so e passado por parametro valores digitados pelos usuarios                
        #aqui teremos nossos atributos
        

            #Instancia
        self.cliente  = Cliente(nome_cliente, cpf_cliente, tipo_conta)#O self aqui foi usado para definir como uma variavel que tera varios dados que pertence ao a variavel cliente
        #usamos o self para armazenar de forma prolongada os dados que estao sendo passados

    def salvar_excel(self, caminho_excel):
        dados_clientes = self.cliente.dicionario_cliente()

        excel = pd.DataFrame(dados_clientes)

        return excel