from Conta import Conta

class ContaCorrenteEspecial(Conta):
    def __init__(self, agencia, conta, saldo, LimiteContaEspecial = 1000):
        super().__init__(agencia,conta,saldo)
        self.LimiteContaEspecial = LimiteContaEspecial

    def saqueEspecial(self,valor):
        saldo_especial = self.getSaldo() + self.LimiteContaEspecial

        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        
        if valor <= saldo_especial:
            self.setSaldo(self.getSaldo() - valor)
            return True
        else:
            print("Saldo Indisponivel para saque.")
            return False
        