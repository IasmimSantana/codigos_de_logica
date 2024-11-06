matriz =[[0,0,0,0,], [0,0,0,0],[0,0,0,0,]]
while True:
    andar = int(input("Qual o andar do quarto?"))
    quarto= int(input("Qual o numero do quarto?"))
    reserva= matriz[quarto-1][andar-1]
    if reserva !=0:
         print("Quarto reservado")
    else:
       print("Quarto liberado")
       print("Farei uma reserva:")
       matriz[quarto-1][andar-1] = 1
       print("O quarto foi reservado")
       print("reservado")
       break