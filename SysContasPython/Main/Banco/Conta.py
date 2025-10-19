class Conta:
    def __init__(self, agencia, conta, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    def setAgencia(self, agencia):
        self.__agencia = agencia

    def setConta(self, conta):
        self.__conta = conta

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getAgencia(self):
        return self.__agencia

    def getConta(self):
        return self.__conta

    def getSaldo(self):
        return self.__saldo

    def depositar(self, valor):
        if (valor > 0):
            self.__saldo = self.__saldo + valor
            return True
        else:
            print("Valor inválido para depósito.")
            return False
    
    def sacar(self, valor):
        if (valor > 0): 
            if (valor <= self.__saldo):
                self.saldo = self.__saldo - valor
                return True   
            else:
                print("Saldo Insuficiente!")
                return False
        else:
            print("Valor inválido para saque.")
            return False
        
    def verSaldo(self):
        return self.getSaldo()
