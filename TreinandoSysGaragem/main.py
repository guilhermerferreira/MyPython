#Programa Basico Gagagem

class Carro:
    def __init__(self,marca,modelo,potencia,disponivel = True):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.disponivel = disponivel

    def __str__(self):
        status = 'Disponivel' if self.disponivel else 'Indisponivel'
        return (f'{self.marca} - {self.modelo} - {self.potencia} cavalos - {status}')
    

class Garagem:
    def __init__(self):
        self.garagem = []

    def adicionar_carro(self,carro):
        self.garagem.append(carro)

    def consultar_carro(self,marca):
        for carro in self.garagem:
            if carro.marca.lower() == marca.lower():
                return carro
        return None
    
    def mostrar_estoque(self):
        if not self.garagem:
            print('\nNenhum carro na garagem.')
        else:
            print('\nCarros na garagem: ')
            for carro in self.garagem:
                print(carro)
    
    def alugar_carro(self,marca):
        carro = self.consultar_carro(marca)
        if carro:
            if carro.disponivel:
                carro.disponivel = False
                print(f'\nVoce alugou o carro {carro.marca}')
            else:
                print('\nCarro ja alugado por outra pessoa.')
        else:
            print('\nCarro nao encontrado!')

    def devolver_carro(self,marca):
        carro = self.consultar_carro(marca)
        if carro:
            if not carro.disponivel:
                carro.disponivel = True
                print(f'\nVoce devolveu o carro {carro.marca}. Obrigado!!')
            else:
                print('\nCarro ja devolvido!')
        else:
            print('\nCarro nao encontrado!')

garagem = Garagem()
garagem.adicionar_carro(Carro('Audi', 'R8', 610))
garagem.adicionar_carro(Carro('BMW', 'M4', 510))
garagem.adicionar_carro(Carro('Ferrari', '488', 670))

while True:
    print("\n#### GARAGEM ####")
    print("1 -- Consultar Carro")
    print("2 -- Ver Carros da Garagem.")
    print("3 -- Alugar Carro.")
    print("4 -- Devolver Carro.")
    print("0 -- Sair.")
    opcao = input('\nDigite a opcao: 1/2/3/4/0: ')

    if opcao == "1":
        marca = input('Digite a marca do carro que deseja consultar: ')
        carro = garagem.consultar_carro(marca)
        if carro:
            print(f'\nCarro encontrado - {carro}')
        else:
            print('\nCarro nao encontrado')
    
    elif opcao == "2":
        garagem.mostrar_estoque()

    elif opcao == "3":
        marca = input('\nDigite a marca do carro que deseja alugar: ')
        carro = garagem.alugar_carro(marca)
        
    elif opcao == "4":
        marca = input('\nDigite a marca do carro que deseja devolver: ')
        carro = garagem.devolver_carro(marca)

    elif opcao == "0":
        print('\nSaindo da Garagem...')
        break

    else:
        print('\nOpcao Invalida!!')