# AQRUIVO CSV
import csv

with open("arquivos/numeros.csv", "w") as arquivo:

  #Cria o  objeto de gravacao
  writer = csv.writer(arquivo)
  #Grava no arquivo linha a linha
  writer.writerow(("nota1", "nota2", "nota3"))
  writer.writerow((63, 87, 92))
  writer.writerow((61, 79, 76))
  writer.writerow((72, 64, 91))
  
#Leitura de arquivo CSV
with open("arquivos/numeros.csv", "r", encoding="utf-8", newline = '\r\n') as arquivo:
  #Cria o objeto leitura
  leitor = csv.reader(arquivo)
  #Loop
  for x in leitor:
    print(x)
    
#Gerando lista com dados do arquivo CSV
with open("arquivos/numeros.csv", "r") as arquivo:
  leitor = csv.reader(arquivo)
  dados = list(leitor)
print("\n", dados, "\n")
#Imprimindo dados a partir da segunda linha
for linha in dados[1:]:
  print(linha)