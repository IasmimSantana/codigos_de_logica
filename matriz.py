def contar(matriz):
    contagem = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
               contagem += 1
    return contagem          
matriz = [[5,12,7,20],
          [15,8,22,10],
          [9,11,6,14,],
          [13,25,3,9]]
resultado = contar(matriz)
print(f"Quantidade de valores maiores que 10: {resultado}")

