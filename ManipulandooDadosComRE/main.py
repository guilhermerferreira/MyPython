import re

texto = 'Meu e-mail e exemplo@gmail.com e voce pode contatar em outro_email@yahoo.com.'
resultado = len(re.findall('@', texto))
print(f'O caractere @ apareceu {resultado} vezes')


resultado = re.findall(r'voce (\w+)', texto)
print(f'A palavra apos "voce" e: {resultado[0]}')


email = re.findall(r'(?<!\S)[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b', texto)
print(email)


musica = '''
Todos os dias quando acordo
Não tenho mais o tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo que esse sangue amargo
E tão sério
E selvagem!
Selvagem!
Selvagem!
Veja a tempestade sol dessa manhã tão cinza
A que chega é da cor dos teus olhos
Castanhos
Então me abraça forte
Me diz mais uma vez que já estamos
Distantes de tudo
Temos nosso
próprio tempo Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas
Agora
O que foi escondido é o que se escondeu
E o que foi prometido, ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens
Tão jovens
'''

resultado1 = len(re.findall('a',musica))
print(f'\nA letra "a" aparece {resultado1} vezes')

resultado2 = len(re.findall('tempo',musica))
print(f'A palavra "texto" aparece {resultado2} vezes')

resultado3 = re.findall(r'\b\w+!',musica)
print(f'As palavras seguidas por expressao sao: {resultado3}')

resultado4 = len(re.findall('forte', musica))
print(f'A palavra "forte" aparece {resultado4} vezes')

resultado5 = re.findall(r'\b[EeéÉ]\s+(\w+)',musica)
print(resultado5)