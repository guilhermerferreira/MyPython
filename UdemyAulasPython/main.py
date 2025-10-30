# # ARRAY

# from array import array

# lista1 = ['a', 'b', 'c', 'd', 'e']

# lista1 = array('w', ['a', 'b', 'c', 'd', 'e'])

# print(lista1)
# print(list(lista1))


# #     #       #       #       #


# # SET
#     # Similiar a listas
#     # Evita itens duplicados
#     # Nao utiliza index

# lista1 = [10, 20, 30, 40, 50]
# lista2 = [10, 20, 60, 70]

# num1 = set(lista1)
# num2 = set(lista2)

# print(num1 | num2) # Union
# print(num1 - num2) # Difference
# print(num1 ^ num2) # Symmetric Difference
# print(num1 & num2) # And


#  #     #       #       #       #


# # Funcao em SET 

# s1 = {1, 2, 3, 5, 6}

# s1.update([6,7,8,9,10])
# s1.remove(1)
# s1.discard(90)

# print(s1)


#       #       #       #       #


# # SET com string

# set1 = {'a', 'b', 'c'}
# set2 = {'a', 'd', 'e'}
# set3 = {'c', 'd', 'f'}

# set4 = set1.union(set2)
# set5 = set1.difference(set2)
# set6 = set1.intersection(set2)


# print(set4)
# print(set5)
# print(set6)


#       #       #       #       #


# # Dicionarios

# aluno = {
#     'nome': 'Guilherme',
#     'idade': 18,
#     'notaFinal': 'A',
#     'aprovacao': True
#     }

# for keys, values in aluno.items():
#     print(keys, values)

# print('\n', aluno.get('cidade', '\nNao existe essa informacao'))

# aluno.update ({'cidade': 'Catanduva'})
# print('\n', aluno.get('cidade'))

# print('\n', aluno.items())
# print('\n', aluno.keys())
# print('\n', aluno.values())


#       #       #       #       #


# # Lambda

# def somar(x,y):
#     func2 = lambda x,y: x + y
#     return func2(x,y) * 5
    
# print(somar(10,20))

#       #       #       #       #


# # Map

# #lista1 = [2,4,6,8,10]

# def mult(x):
#     return x*2

# lista2 = map(mult, lista1)

# #print(list(map(lambda x: x * 2, lista1)))


#       #       #       #       #


# # Filter

# #####
# valores = [10,12,34,44,57]

# #print(list(filter(lambda x: x > 20, valores)))
# #####

# #####
# def remover20(x):
#     return x > 20

# print(list(filter(remover20,valores)))
# #####

# #####
# frutas1 = ['abacate', 'melao', 'melancia', 'morango', 'abacaxi']
# frutas2 = []

# for itens in frutas1:
#     if 'b' in itens:
#         frutas2.append(itens)

# # List Comprehension
# frutas2 = [itens for  itens in frutas1 if 'm' in itens and 'o' in itens]

# print(frutas2)

# ######
# valores = [x * 10 for x in range(7)]
# print(valores)

# #######
# carros = ['Porsche', 'Ferrari', 'Uno', 'Golf']

# garagem = [cars for cars in carros]

# print(garagem)


#       #       #       #       #


# # Generator Expressions
# from sys import getsizeof

# numeros = (x * 10 for x in range(5))
# print(type(numeros))
# print(getsizeof(numeros))

# print('=====')


# numeros = [x * 10 for x in range(5)]
# print(type(numeros))
# print(getsizeof(numeros))


#       #       #       #       #


# # Erros 
# try:
#     letras = ['a', 'b', 'c', 'd']
#     print(letras[4])
# except IndexError:
#     print('Erro :( Index Nao Existe!')

# try:
#     valor = int(input('Digite o valor do seus produtos: '))
#     print(valor)
# except ValueError:
#     print('Erro :( Favor digitar um valor em numeros')

# try:
#     valor = int(input('Digite o valor do seus produtos: '))
#     print(valor)
# except ValueError:
#     print('Erro :( Favor digitar um valor em numeros')
# finally:
#     print('Ok')
# #else:
#     #print('Usuario digitou um valor correto')
#     #resultado = valor * 2
#     #print(resultado)


# #       #       #       #       #


# # Classes

# from datetime import datetime

# class Funcionarios:
#     def __init__(self,nome,sobrenome,ano_nascimento):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.ano_nascimento = ano_nascimento

#     def nome_completo(self):
#         return f'Nome -- {self.nome} {self.sobrenome}'
    
#     def idade_funcionario(self):
#         ano_atual = datetime.now().year
#         self.ano_nascimento = int(ano_atual - self.ano_nascimento)
#         return self.ano_nascimento
    


# funcionario1 = Funcionarios('Camila', 'Cristina Rodrigues Ferreira', 2007)


# print(funcionario1.nome_completo())
# print(f'Idade -- {funcionario1.idade_funcionario()} anos')



# #       #       #       #       #


# MODULOS

# from funcoes import somar, multi # Importa apenas os metodos que eu seleciono. Nesse caso "somar" e "multi"

# somar()
# multi() 


# Package 
# from items.cadastro import cliente # Importando Package

# cliente()


# from funcoes import find_index

# lista1 = ['a', 'b', 'c', 'd', 'e']

# var1 = find_index(lista1, 'e')
# print(var1)
















    







