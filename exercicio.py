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
    a = int(input("Insira um valor de A:"))
    b = int(input("Insira um valor de B:"))
    c = int(input("Insira um valor de C:"))
    delta = b**2 -4*a*c
    if delta < 0:
        print("O valor da raiz da equação é menor do que zero")
    elif delta == 0:
        x = -b/(2*a)
        print("A equação possui raiz unica")
    else:
        x1 = (-b + raiz(delta))/ (2*a)
        x2 = (-b - raiz(delta))/ (2*a)
        print("As raizes da equação são", x1, "e", x2)
main()