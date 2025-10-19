# Criando um dicionario
dict_guido = {
  'name': 'Guido van Rossum', 
  'linguagem': 'Python',
  'similiar': ['c', 'modula-3', 'lisp'],
  'user': 1000000
}
for k,v in dict_guido.items():
  print(k,v)

#Convertendo um dicionario para json  
import json
json.dumps(dict_guido)

#Criando um arquivo json
with open('arquivos/dados.json', 'w') as arquivo:
  arquivo.write(json.dumps(dict_guido))

#Leitura de um arquivo json
with open('arquivos/dados.json', 'r') as arquivo:
  texto = arquivo.read()
  dados = json.loads(texto)

print(dados['name'])