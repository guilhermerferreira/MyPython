from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, qtdeCheques):
        super().__init__(agencia, conta, saldo)
        self.qtdeCheques = qtdeCheques

    def emitirCheques(self, qtde):
        if ((qtde >0) and (qtde <= self.qtdeCheques)):
            self.qtdeCheques = self.qtdeCheques - qtde
            return True
        else:
            return False
