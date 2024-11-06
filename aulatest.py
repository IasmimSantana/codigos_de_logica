import math
import statistics
import random

def raiz(value):
    return math.sqrt(value)

def fatorial(value):
    return math.factorial(value)

def potencia(value):
    return math.pow(value, 10)

def main():
    numero = random.randint(0,100)
    print("O número sorteado foi:",numero)
    print("A raiz desse número é:", raiz(numero))
    print("O fatorial desse numero é:", fatorial(numero))
    print("A potência(10) do numero é:", potencia(numero))
main()