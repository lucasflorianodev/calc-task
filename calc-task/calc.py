import math

def soma(a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a, b):
    if b == 0:
        raise ValueError("erro, Não existe divisão por 0")
    return a / b

def factorial (n):
    if n < 0:
        raise ValueError("Não existe fatorial de número negativo")
    return math.factorial(n)

def potenciacao(a, b):
    return a ** b