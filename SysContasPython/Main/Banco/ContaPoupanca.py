from Conta import Conta
class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def lancarJuros(self, taxaJuros):
        if (taxaJuros >0.0):
            self.setSaldo(self.getSaldo() + (self.getSaldo()*(taxaJuros/100)))
