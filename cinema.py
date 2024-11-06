def Reservar(sala, fileira, assento):
    if sala[fileira-1][assento-1] == 0:
        sala[fileira-1][assento-1] = 1
        print(f"Voçê reservou um lugar na sala 1, fileira {fileira} , assento {assento}.")
    else:
        print("Esse lugar já está reservado!")

def cancelar_reserva(sala, fileira, assento):
    if sala[fileira-1][assento-1] == 0:
        sala[fileira-1][assento-1] = 1
        print(f"Voçê cancelou a sua reserva na sala 1, fileira {fileira}, assento {assento}")
    else:
        print("Este lugar já está livre")

def exibir_sala(sala):
    for fila in sala:
        print(" ".join(map(str, fila)))

def sair():
    exit
    
sala = [[0] * 8 for fila in range(5)]

print("Cinema")
while True:
    print("MENU:")
    print("1.Fazer reserva")
    print("2.Cancelar reserva")
    print("3.Sair")

    menu = int(input("O que você deseja fazer?"))
    
    if menu == 1:
        fileira = int(input("Qual a fileira?"))
        poltrona = int(input("Qual assento?"))
        Reservar(sala, fileira, poltrona)
        print("MAPA DA SALA")
        exibir_sala(sala)
    elif menu ==2:
        cancelar_reserva(sala, fileira, poltrona)
    elif menu == 3:
        sair()
    else:
        print("O código não é válido!")
       




