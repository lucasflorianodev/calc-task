import pytest
from calc import soma, subtracao, multiplicacao, divisao, factorial, potenciacao

def test_soma():
    assert soma(1,2) == 3   # soma de números inteiros;
    assert soma(3,5) == 8   # soma de números primos;
    assert soma(-1,1) == 0  # soma por número negativo;

def test_subtracao():
    assert subtracao(7,4) == 3  # subtração de numeros inteiros;
    assert subtracao(-5,2) == -7    # subtração de negativo com positivo;
    assert subtracao(-2,-3) == 1    # subtração de números negativos;
    assert subtracao(2.5,3.5) == -1.0   #subtração de números reais
    assert subtracao(5,0) == 5  #subtração por 0.

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6 # multiplicação de números inteiros;
    assert multiplicacao(-1, 5) == -5   # multiplicação de por número negativo;
    assert multiplicacao(0, 10) == 0    # multiplicação de número por 0;
    assert multiplicacao(13.2, 2) == 26.4   #multiplicação de números rais.

def test_divisao():
    assert divisao(10, 2) == 5  #divisão de números inteiros.
    assert divisao(9, 3) == 3   #divisão de números múltiplos.
    with pytest.raises(ValueError): # teste de divisão por 0
        divisao(10, 0)

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):  # tentativa de fatorial de número negativo
        factorial(-5)

def test_potenciacao():
    assert potenciacao(2, 3) == 8
    assert potenciacao(5, 0) == 1
    assert potenciacao(2, -2) == 0.25