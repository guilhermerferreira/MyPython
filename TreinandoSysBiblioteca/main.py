# Programa Basico para Biblioteca em POO com Python 

class Livro:
    def __init__(self, titulo, autor, paginas, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = disponivel

    def __str__(self):
        status = 'Disponivel' if self.disponivel else 'Indisponivel'
        return (f'{self.titulo} - {self.autor} - {self.paginas} paginas - {status} ')

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self,livro):
        self.livros.append(livro)

    def consultar_livro(self,titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro	
        return None	
        
    def mostrar_repertorio(self):
        if not self.livros:
            print('\nNenhum livro cadastrado.')
        else:
            print('\nRepertorio de Livros:')
            for livro in self.livros:
                print(livro)
	
    def pegar_livro(self, titulo):
        livro = self.consultar_livro(titulo)
        if livro:
            if livro.disponivel:
                livro.disponivel = False
                print(f'\nVoce pegou o livro "{livro.titulo}".')
            else:		
                print('\nEsse livro ja foi emprestado.')
        else:
            print('Livro nao encontrado.')

    def devolver_livro(self,titulo):
        livro = self.consultar_livro(titulo)
        if livro:
            if not livro.disponivel:
                livro.disponivel = True
                print(f'\nVoce devolveu o livro "{livro.titulo}". Thanks!!')
            else:
                print('\nEste livro ja esta disponivel na biblioteca.')
        else:
            print('\nLivro nao encontrado.')
            

biblioteca = Biblioteca()

biblioteca.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis", 250))
biblioteca.adicionar_livro(Livro("O Senhor dos Aneis", "J.R.R. Tolkien", 1200))
biblioteca.adicionar_livro(Livro("Python para Iniciantes", "Guido Van Rossum", 350))

while True:
    print('\n##### BIBLIOTECA #####')
    print('1 -- Consultar Livro.')
    print('2 -- Repertorio.')
    print('3 -- Pegar Livro.')
    print('4 -- Devolver Livro.')
    print('0 -- Sair')
    opcao = input('\nDigite a opcao 1/2/3/4: ')

    if opcao == "1":
        titulo = input('Digite o livro que deseja: ')
        livro = biblioteca.consultar_livro(titulo)
        if livro:
            print(f'\nLivro encontrado: "{livro}".')
        else:
            print('\nLivro nao encontrado.')

    elif opcao == "2":
        biblioteca.mostrar_repertorio()

    elif opcao == "3":
        titulo = input('\nDigite a opcao do livro que deseja pegar: ')
        biblioteca.pegar_livro(titulo)

    elif opcao == "4":
        titulo = input('Digite o livro que deseja devolver: ')
        biblioteca.devolver_livro(titulo)

    elif opcao == "0":
        print("Saindo da biblioteca...")
        break

    else:
        print('Opcao invalida!')
