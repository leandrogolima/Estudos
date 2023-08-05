class ContaCorrente():
    def __init__(self, nome: str, cpf:int, agencia:int, num_conta:int) -> None:
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta

    def Consultar_saldo(self):
        print('O seu saldo é de R$ {:,.2f}'.format(self.saldo   ))
        pass
    
    def Deposita(self,valor):
        self.saldo += valor
        pass

    def Sacar(self,valor):
        if self.saldo - valor < self.Limite_conta():
            print('Saldo insuficiente\nSaldo atual R$ {:,.2f}\nSeu limite é de R$ {:,.2f}'.format(self.saldo,self.limite))
        else:    
            self.saldo -= valor
        pass

    def Limite_conta(self):
        self.limite = -1000
        return self.limite


leandro = ContaCorrente('Leandro',111222333)
leandro.Limite_conta()
leandro.limite
leandro.Deposita(3250)
leandro.Consultar_saldo()
leandro.Sacar(500)
