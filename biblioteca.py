biblioteca =[] # Vetor Biblioteca

# Função de Add_livro
def adicionar_livro(titulo, ator, genero):
    livro = {'titulo':titulo, 'ator':ator, 'genero':genero, 'disponivel':True}
    biblioteca.append(livro)
    print(f"O livro {titulo} foi adicionado com sucesso!")

#adicionar_livro('A voz do silencio', 'Any', 'Drama')
#print(biblioteca)

def remover_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'] ==  titulo:
            biblioteca.remove(livro)
            print(f"O livro {titulo} foi removido com sucesso!")

def buscar_livro(busca):
    for livro in biblioteca:
        if livro ['titulo'] == busca or livro ['autor'] == busca or livro ['genero']: 
            print("Resultado da Busca:\n")
            print(f"Livro: {livro['titulo']} | Autor: {livro['autor']} | Genero: {livro['genero']} - Status: {livro['disponivel']}")
            return
        else:
            print("Livro não encontrado!")
def listar_livro():
    if not biblioteca:
        print("Nenhum livro encontrado")
    else:
        print(f"lista de livros: \n")
        for  livro in biblioteca:
              if livro['disponivel'] == True:
                  status = 'Disponivel'
              else:
                  status = 'Indisponivel'
                  print(f"Livro: {livro['titulo']} | Autor: {livro['autor']} | Genero: {livro['genero']} - Status:{status}")
def mostrar_menu():
    print("OPÇÕES DO SISTEMA DE BIBLIOTECA")
    print("1.Adicionar livro")
    print("2.Remover livro")
    print("3.Buscar livro")
    print("4.Listar livro")
    print("5.Verificar Disponibilidade")
    print("6.Sair")
while True:
    mostrar_menu()
    escolha= int(input("Escolha uma opção do menu: "))
    if escolha == 1:
        titulo = input("Digite o Titulo do Livro: \n")
        autor = input("Digite o nome do autor:\n")
        genero = input("Digite o genero do livro: \n")
        adicionar_livro(titulo, autor, genero)
    elif escolha == 2:
        titulo = input("Digite o Titulo do Livro que deseja remover: \n")
        remover_livro(titulo)
    elif escolha == 3:
        titulo = input("Digite o Titulo do Livro que deseja encontrar: \n")
        buscar_livro(titulo)
    elif escolha == 4:
        titulo = input("Listar todos os livros: \n")
        listar_livro()
    elif escolha == 5:
        #titulo = input("Digite o título do livro para verificar disponibilidade:\n ")
        print("Funçao não disponivel")
    elif escolha == 6:
        titulo = input("Emprestimo de livro:\n ")
        #IMPLEMENTAR ESSA FUNÇÃO
        #emprestimo_livro(titulo,autor)
    else:
        print("Fechando o Sistema...")
        break
