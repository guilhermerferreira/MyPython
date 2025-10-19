# Treinando random, jogo de números em Python


import  random as rd

numeros = rd.sample(range(50),10)	            

print('🎰🎰🎰🎰🎰🎰 BEM VINDO AO JOGO DE ADIVINHAÇÃO 🎰🎰🎰🎰🎰🎰')
print('\n50 numeros serao sorteados, sua missao é adivinhar um deles. \nVocê tem 5 tentativas, Boa sorte!')
print(input('\n🎰🎰🎰🎰🎰Tecle "Enter" para comecar o jogo🎰🎰🎰🎰🎰'))

tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
  chute = int(input('🍀Digite um numero🍀: '))
  tentativas += 1
  
  if chute in numeros:
    print(f'\n🎉Parabens, você acertou! o numero {chute} estava na lista🎉')
    print(f'Os numeros sorteados eram: {numeros}')
    break

  else:
    print(f'\n❌Você errou, restam - {max_tentativas - tentativas} tentativas❌')
    
if tentativas == 5 and chute not in numeros:
  print('\n💀GAME OVER! Você não conseguiu adivinhar nenhum numero💀')
  print(f'\nOs numeros sorteados eram: {numeros}')