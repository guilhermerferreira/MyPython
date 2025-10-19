# Calculadora em Python

print("############## CALCULADORA EM PYTHON ##############")
print("1 -- Soma")
print("2 -- Subtracao")
print("3 -- Multiplicacao")
print("4 -- Divisao")

soma = lambda x,y: x + y
subtracao = lambda x,y: x - y
multiplicacao = lambda x,y: x * y
divisao = lambda x,y: x / y

escolha = int(input("\nDigite sua opcao (1/2/3/4): "))

if escolha == 1:
  x = int(input('Digite o primeiro numero: '))
  y = int(input('Digite o segundo numero: '))
  print(f"\n{x} + {y} = {soma(x,y)}")


elif escolha == 2: 
  x = int(input('Digite o primeiro numero: '))
  y = int(input('Digite o segundo numero: '))
  print(f"\n{x} - {y} = {subtracao(x,y)}")


elif escolha == 3:
  x = int(input('Digite o primeiro numero: '))
  y = int(input('Digite o segundo numero: '))
  print(f"\n{x} * {y} = {multiplicacao(x,y)}")


elif escolha == 4:
  x = int(input('Digite o primeiro numero: '))
  y = int(input('Digite o segundo numero: '))
  print(f"\n{x} / {y} = {divisao(x,y)}")

else:
  print("Opcao invalida!!")