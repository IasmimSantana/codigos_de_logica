artistas = ["Roberto Carlos", "Luiz Gonzaga", "Billie", "Taylor Swift"]
def novo_artista(novo):
    artistas.append(novo)
    print("\n O Artista: ",novo," foi inserido na lista.")
    print("\n A lista nova ficou assim:",artistas)
    
    
def sub_artista(antigo, novo):
    indice = artistas.index(antigo)
    artistas[indice] = novo
    print("\n O Artista: ",antigo," foi substituido pelo novo artista,",novo)
    print("\n A nova lista é: ",artistas)
    
def lista_atual():    
    print("\n A nova lista é: ",artistas)

def quantidade_artistas():
    cont = len(artistas)
    print("\n A quantidade é:", cont)

def remover(nome):
    artistas.remove(nome)
    print("\n O Artista: ",nome," foi removido")
    print("\n A nova lista é: ",artistas) 

def sair():
    exit

    
print("------- SISTEMA DE AGENDAMENTO DE SHOWS! ----------")
while True:
    print("MENU:")
    print("1.INSERIR NOVO ARTISTAS NA LISTA")
    print("2.SUBSTITUIR ARTISTA DA LISTA")
    print("3.LISTA ATUAL")
    print("4.QUANTIDADE DE ARTISTAS")
    print("5.REMOVER")
    print("6.SAIR")
    
    
    menu = int(input("O que você deseja fazer?"))
    
    if menu == 1:
        #insere o novo artista no final da lista 
        novo = input("Insira o nome do novo artista: ")
        novo_artista(novo)
        
    elif menu == 2:
        antigo = input("Insira o nome do artista que será removido: ")
        novo = input("Insira o nome do artista que será o inserido no lugar: ")
        #subistitui o nome do novo artista
        sub_artista(antigo,novo)
            
    elif menu == 3:
        lista_atual()
    
    elif menu == 4:
         quantidade_artistas()

     
    elif menu == 5:
        nome = input("Insira o nome do artista que deseja remover: ")
        remover(nome)

    elif menu == 6:
        sair()
    else:
        print("O código não é válido!")