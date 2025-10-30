                                        # DESAFIOS #

# ------------------------------------------------------------------------------------- #
                            # DESAFIO TEMPERATURA DA CARNE #

# temperatura= int(input('Digite a temparatura da carne em celsius? '))
# def ponto_carne():
#     if temperatura < 48:
#         print('A carne esta CRUA!')
#     elif temperatura in range(48, 53):
#         print ('A carne esta SELADA!')
#     elif temperatura in range(54, 59):
#         print('A carne esta ao PONTO para o MAL!')
#     elif temperatura in range(60, 64):
#         print('A carne esta ao PONTO!')
#     elif temperatura in range(65, 70):
#         print('A carne esta BEM PASSADA!')
#     elif temperatura in range(71, 77):
#         print('A carne esta SELADA!')
#     else:
#         print('A carne esta QUEIMADA!')
#     return
               
# ponto_carne()

# ------------------------------------------------------------------------------------- #
                              # DESAFIO RENDIMENTO #


# rendimento = int(input('Qual o rendimento da lata? '))
# altura = int(input('Qua a altura da parede? '))
# largura = int(input('Qual a largura da parede? ')) 
#  
# def latasDeTintas():
#     qtdLata = (largura * altura) / rendimento
#     print(f'Voce precisara de {qtdLata} latas de tinta.')

# latasDeTintas()

# ------------------------------------------------------------------------------------- #
                            # DESAFIO FUNCIONARIOS #

# funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
# turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
# turno_noite = ['Pedro', 'Sophia', 'Bruno']
# tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# # FUNCIONARIOS DO TURNO DA NOITE QUE POSSUEM CARRO
# lista1 = set(turno_noite).intersection(tem_carro)
# # FUNCIONARIOS DO TURNO DO DIA QUE POSSUEM CARRO
# lista2 = set(turno_dia).intersection(tem_carro)
# # FUNCIONARIOS QUE NAO POSSUEM CARRO
# lista3 = set(funcionarios).difference(tem_carro)

# print(f'Lista de funcionarios do turno da noite que possuem carro: {lista1}')
# print(f'Lista de funcionarios do turno do dia que possuem carro: {lista2}')
# print(f'Lista de funcionarios que nao possuem carro: {lista3}')

# ------------------------------------------------------------------------------------- #
                                # DESAFIO IMC #

# altura = float(input('Digite sua altura em metros: '))
# peso = float(input('Digite seu peso em kg: '))

# imc = peso / (altura * altura)

# if imc < 18.5:
#     print('Abaixo do peso')
# elif 18.5 <= imc < 25:
#     print('Peso normal')
# elif 25 <= imc < 30:
#     print('Sobrepeso')
# elif 30 <= imc < 35:
#     print('Obesidade grau I')
# elif 35 <= imc < 40:
#     print('Obesidade grau II')
# else:
#     print('Obesidade grau III')

# ------------------------------------------------------------------------------------- #

# --------------------------------------RELEMBRANDO------------------------------------ #

# ------------------------------------------------------------------------------------- #

                                    # INSERT, REMOVE, DEL #

# frutas = ['banana', 'abacate', 'melancia']
# frutas.insert(2, 'Mamao')
# frutas.remove('banana')
# del frutas[-1]
# print(frutas)

# ------------------------------------------------------------------------------------- #
                                    # NEXTED FOR LOOP #

# frutas = ['banana', 'abacate', 'melancia']
# vegetais = ['brocolis', 'cenoura', 'tomate', 'alface']

# for fruta in frutas:
#     for vegetal in vegetais:
#         print(fruta, vegetal)

# ------------------------------------------------------------------------------------- #
                                        # WHILE LOOP #

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# ------------------------------------------------------------------------------------- #
                                   # BREAK AND CONTINUE #

# for num in range(1,50):
#     if num == 30:
#         break
#     print(num)

# for i in range (1,50):
#     if i == 10:
#         continue
#     print(i)

# ------------------------------------------------------------------------------------- #
                                        # COUNT #

# vegetais = ['brocolis', 'cenoura', 'cenoura', 'cenoura', 'tomate', 'alface']
# count = 0

# for vegetal in vegetais:
#     if vegetal == 'cenoura':
#         count += 1

# print(f'Numero de cenouras na lista: {count}')

# ------------------------------------------------------------------------------------- #
                                    # WHILE CONDICIONAL #

# while True:
#     fruta = input('Adivinhe a fruta: ').lower() 
#     if fruta == 'abacate':
#         print('Parabens, voce acertou a fruta!')
#         break

# ------------------------------------------------------------------------------------- #
                                    # PAR AND IMPAR #

# numeros = list(range(1,22))
# for num in numeros:
#     if num % 2 == 0:
#         print(f'O numero {num} e par!')
#     else:
#         print(f'O numero {num} e impar!')

# ------------------------------------------------------------------------------------- #
                                    # DICIONARIO #

# capitais = {
#     'Brasil': "Brasilia",
#     'Argentina': 'Buenos Aires',
#     'Chile': 'Santiago',
#     'Australia': 'Camberra',
#     'Canada': 'Otawwa'
#     }

# pais = input('Digite o nome do pais: ')
# if pais in capitais:
#     print(f'A capital de {pais} e {capitais[pais]}')
# else:
#     print('Desculpe :( nao temos essa informacao!)')

# ------------------------------------------------------------------------------------- #
                         # SET IMPRIMINDO NOMES REPETIDOS #

# funcionarios1 = ['Gabriel', 'Claudio', 'Ana', 'Camila', 'Joao']
# funcionarios2 = ['Ana', 'Guilherme', 'Camila', 'Pedro', 'Joao']

# resultado = set(funcionarios1).intersection(funcionarios2)
# print(resultado)

# ------------------------------------------------------------------------------------- #
                                # FUNCAO QUADRADO #

# def quadrado(num):
#     return num ** 2

# num = int(input('Digite um numero: '))
# print(f'O valor de {num} ao quadrado e: {quadrado(num)}')

                                
                                   # POTENCIA #
# def potencia(base,exp=2):
#     if base and exp:
#         return base ** exp
    
# num = int(input('Digite o numero base: '))               
# expo = input('Digite um exponente (default 2): ')       

# if expo:
#     print(f'O resultado e {potencia(num, int(expo))}')  
# else:
#     print(f'O resultado e {potencia(num)}')      

# ------------------------------------------------------------------------------------- #
                             # USANDO RECURSIVIDADE # FATORIAL #

# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#        return n * fatorial(n - 1)

# num = int(input('Digite um numero: '))
# print(f'O fatorial de {num} e: {fatorial(num)}')

                            # LOOP COM RECURSAO #
# def loop(ini,fim):
#     if ini > fim:
#         return
#     else:
#         print(ini)
#         loop(ini+1,fim)

# loop(10,20)

# ------------------------------------------------------------------------------------- #
                                # FUNCAO EM FUNCAO #

# def dobrar(num):
#     return num*2

# def quadrado(num):
#     return dobrar(num) ** 2

# num = int(input('Digite um numero: '))
# print(f'O quadrado do dobro do numero {num} e {quadrado(num)}')

# ------------------------------------------------------------------------------------- #
                                # LAMBDA #

                              # LAMBDA CUBO #
# cubo = lambda num: num ** 3
# num = int(input('Digite um numero: '))
# print(f'O cubo de {num} e -> {cubo(num)}')

                              # LAMBDA MULTI #
# mult = lambda x,y: x * y
# num1 = int(input('Digite um numero: '))
# num2 = int(input('Digite o multiplicador: '))
# print(f'A multiplicacao de {num1}*{num2} e {mult(num1,num2)}')

                              # LAMBDA IF ELSE #
# par_or_impar = lambda x: 'Par' if x % 2 == 0 else 'Impar'
# num = int(input('Digite um numero: '))
# print(f'O Numero {num} e {par_or_impar(num)}')
    
                              # LAMBDA FOR LOOP #
# numeros = [1, 2, 3, 4, 5, 6]
# quadrado = lambda x: x ** 2
# resultados = []

# for num in numeros:
#     resultados.append(quadrado(num))

# print(f'Os quadrados dos numeros {numeros} sao {resultados}')
                            










    
    























    


