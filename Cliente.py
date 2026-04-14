#aqui temos a evolucao de um dicionario sendo agora uma classe com uma funcao. acaba sendo a evolucao do dicionario por conta da sua locomocao sendo ser transferidos por arquivos diferente do dicionario comum

class Cliente:
    
    #Temos uma funcao usando __init__(construtor) servindo para criara um moude dos dados dos clientes com o objetivo de conseguir transferir dados por todos os arquivos python
    def __init__(self, nome_cliente, cpf_cliente, tipo_conta,numero_conta, agencia, extrato):
        
        #chamamos essas variaveis de atributos por ser no formato __init__ quando colocamos self antes da variavel para informar que aquela variavel sera do nosso moude como em um dicionario chave e valor, o que estiver com self e chave e sem o self valor "variavel"        
        self.nome_cliente =  nome_cliente
        self.cpf_cliente = cpf_cliente
        self.tipo_conta = tipo_conta
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.extrato = extrato

    #criamos uma nova funcao usando o __STR__ para transforma os dados em string para que seja printado da forma correta no terminal
    def __str__(self):
        return f"Nome: {self.nome_cliente} | CPF: {self.cpf_cliente}| Conta: {self.tipo_conta} | Numero_conta: {self.numero_conta} | Agência: {self.agencia} | Extrato: {self.extrato}" 





