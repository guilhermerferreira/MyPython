# Jogo da Forca em POO com Python

import random
from os import system, name 

#funcao para limpar a tela a cada execucao
def limpa_tela():
    #Windows
    if name == 'nt':
        _=system('cls')

# Tabuleiro (estágios da forca)
tabuleiro = ['''

>>>>>>>>>> Jogo da Forca <<<<<<<<<<

+---+	
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Forca:
    def __init__(self,palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    def chute(self,letra):
        
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)

        else:
            return False
        
        return True 
    
    # Método para verificar se o jogo terminou
    def fim_de_jogo(self):
        return self.jogo_ganho() or (len(self.letras_erradas) == 6)
    
    # Método para verificar se o jogador venceu
    def jogo_ganho(self):

        if '_' not in self.mostrar_letra():
            return True
        return False
    
    # Método para não mostrar a letra no board
    def mostrar_letra(self):

        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
    
    # Método para checar o status do game e imprimir o board na tela
    def printando_game(self):
        print(tabuleiro[len(self.letras_erradas)])
        print('\nPalavra: ' + self.mostrar_letra())
        print('\nLetras erradas: ',)

        for letra in self.letras_erradas:
            print(letra,)

        print()

        print ('Letras corretas: ',)

        for letra in self.letras_escolhidas:
            print(letra,)

        print()

# Método para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():

    # Lista de palavras para o jogo
    lista_palavras = ['batman', 'coringa', 'pinguim', 'charada']
    # Escolhe randomicamente uma palavra
    palavra = random.choice(lista_palavras)
    
    return palavra
    
# Método Main - Execução do Programa
def main():
        
    limpa_tela()

    # Cria o objeto e seleciona uma palavra randomicamente
    game = Forca(palavra_aleatoria())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.fim_de_jogo():

        #status do game
        game.printando_game()
        # Recebe input do terminal
        digito_usuario = input('\nDigite uma letra: ')

        # Verifica se a letra digitada faz parte da palavra
        game.chute(digito_usuario)
    
    # Verifica o status do jogo
    game.printando_game()
    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.jogo_ganho():
        print('\nParabens! Voce ganhou!')
    else:
        print ('\nGame over! Você perdeu.')
        print ('A palavra era ' + game.palavra)

# Executa o programa		
if __name__ == "__main__":
	main()
