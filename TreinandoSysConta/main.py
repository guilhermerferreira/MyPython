class Conta:
    def __init__(self,agencia,conta,saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def __str__(self):
        return f"\nAgência: {self.agencia} | Conta: {self.conta} | Saldo: R${self.saldo:.2f}"

    def depositar(self,valor):
        if valor > 0.0:
            self.saldo += valor
            print(f'\nValor depositado! Novo saldo: R${self.saldo:.2f}')
            return True
        else:
            print('\nValor invalido para deposito. Necessario ser maior que 0')
            return False
        
    def sacar(self,valor):
        if valor > 0.0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Valor sacado com sucesso! Novo saldo: R${self.saldo:.2f}')
                return True
            else:
                print('\nSaldo Insuficiente.')
                return False
        else:
            print('\nValor invalido para saque. Necessario ser maior que 0')
            return False
    
    def verSaldo(self):
        return f'\nSaldo total: R${self.saldo:.2f}'
    

########################################################################

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo,qtdCheques):
        super().__init__(agencia, conta, saldo)
        self.qtdCheques = qtdCheques

    def __str__(self):
        return super().__str__() + f' | Cheques disponiveis: {self.qtdCheques}'

    
    def adicionarCheques(self,qtd):
        if qtd > 0:
            self.qtdCheques += qtd
            print(f'\nCheque(s) adicionado(s)! Total: R${self.qtdCheques}')
            return True

   
    def emitirCheques(self,qtd):
        if qtd > 0 and qtd <= self.qtdCheques:
            self.qtdCheques -= qtd
            print(f'\nCheque(s) emitido(s)! Restam {self.qtdCheques} cheques.')
            return True
        else:
            print('\nQuantidade de cheques invalida ou insuficiente.')
            return False
        

########################################################################

class ContaPoupanca(Conta):
    def __init__(self,agencia,conta,saldo):
        super().__init__(agencia,conta,saldo)

    def lancarJuros(self,taxaJuros):
        if taxaJuros > 0.0:
            self.saldo += self.saldo * (taxaJuros/100)
            print(f'\nJuros de {taxaJuros} aplicado! Novo saldo: R${self.saldo:.2f}')
            return True
        else:
            print('\nTaxa de juros invalida. Necessario ser maior que 0')


########################################################################

class ContaSalario(Conta):
    def __init__(self,agencia,conta,saldo):
        super().__init__(agencia,conta,saldo)

    def lancarPagamento(self,valor):
        if valor > 0.0:
            self.saldo += valor
            print(f'\nPagamento lancado! Novo saldo: R${self.saldo:.2f}')
            return True
        else:
            print('\nValor invalido. Necessairo ser maior que 0')
            return False
########################################################################      


########################################################################
contaCorrente = ContaCorrente('0001', '0101', 5325.50, 30)
contaPoupanca = ContaPoupanca('0002', '3101' , 631.73 )
contaSalario = ContaSalario('0003', '1331', 1521.90 )
########################################################################


while True:
    print('\n--- BANCO ---')
    print('1 -- Conta Corrente.')
    print('2 -- Conta Poupanca.')
    print('3 -- Conta Salario.')
    print('0 -- Sair')
    opcao = input('\nDigite a opcao 1/2/3/0: ')


########################################################################

    if opcao == "1":
        while True:
            print('\n--- CONTA CORRENTE ---')
            print('1 -- Realizar Depósito')
            print('2 -- Realizar Saque')
            print('3 -- Ver Saldo')
            print('4 -- Emitir Cheques')
            print('5 -- Ver detalhes da conta')
            print('0 -- Voltar')
            opc = input('\nDigite a opção: ')

            if opc == "1":
                valor = float(input('\nDigite o valor que deseja depositar: '))
                contaCorrente.depositar(valor)

            elif opc == "2":
                valor = float(input('\nDigite o valor que deseja sacar: '))
                contaCorrente.sacar(valor)

            elif opc == "3":
                print(contaCorrente.verSaldo())

            elif opc == "4":
                qtd = int(input('\nDigite a quantidade de cheques: '))
                contaCorrente.emitirCheques(qtd)
            
            elif opc == "5":
                print(contaCorrente)

            elif opc == "0":
                break
            
            else:
                print('\nOpção inválida!')

########################################################################

    elif opcao == "2":
        while True:
            print('\n--- CONTA POUPANCA ---')
            print('1 -- Realizar Depósito')
            print('2 -- Realizar Saque')
            print('3 -- Ver Saldo')
            print('4 -- Aplicar Juros')
            print('5 -- Ver detalhes da conta')
            print('0 -- Voltar')
            opc = input('\nDigite a opção: ')

            if opc == "1":
                valor = float(input('\nDigite o valor que deseja depositar: '))
                contaPoupanca.depositar(valor)

            elif opc == "2":
                valor = float(input('\nDigite o valor que deseja sacar: '))
                contaPoupanca.sacar(valor)

            elif opc == "3":
                print(contaPoupanca.verSaldo())

            elif opc == "4":
                taxa = float(input('\nDigite a taxa de juros (%): '))
                contaPoupanca.lancarJuros(taxa)
            
            elif opc == "5":
                print(contaPoupanca)

            elif opc == "0":
                break
            else:
                print('\nOpção inválida!')

########################################################################

    elif opcao == "3":
        while True:
            print('\n--- CONTA SALARIO ---')
            print('1 -- Realizar Saque')
            print('2 -- Ver Saldo')
            print('3 -- Lançar Pagamento')
            print('4 -- Ver detalhes da conta')
            print('0 -- Voltar')
            opc = input('\nDigite a opção: ')

           
            if opc == "1":
                valor = float(input('\nDigite o valor que deseja sacar: '))
                contaSalario.sacar(valor)

            elif opc == "2":
                print(contaSalario.verSaldo())

            elif opc == "3":
                valor = float(input('\nDigite o valor do pagamento: '))
                contaSalario.lancarPagamento(valor)

            elif opc == "4":
                print(contaSalario)

            elif opc == "0":
                break

            else:
                print('\nOpção inválida!')

########################################################################

    elif opcao == "0":
            print('\nSaindo do banco...')
            break
    
    else:
        print('\nOpcao invalida!')
