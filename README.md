# Calculadora Simples em Python

Este projeto contém uma implementação simples de uma calculadora com as operações básicas de soma, subtração, multiplicação, divisão, fatorial e potenciação. O projeto também inclui testes automatizados para garantir que cada operação funcione corretamente.

## Funcionalidades da Calculadora

A calculadora implementa as seguintes operações:

- Soma: Adiciona dois números.
- Subtração: Subtrai o segundo número do primeiro.
- Multiplicação: Multiplica dois números.
- Divisão: Divide o primeiro número pelo segundo. Inclui tratamento para divisão por zero.
- Fatorial: Calcula o fatorial de um número inteiro não negativo. O fatorial de um número negativo gera um erro.
- Potenciação: Calcula o resultado de um número elevado à potência de outro.

## Estrutura do Código

O código da calculadora está implementado no arquivo calculadora.py com a seguinte estrutura de funções:

```python
def soma(a, b):
    # Soma dois números
    return a + b

def subtracao(a, b):
    # Subtrai o segundo número do primeiro
    return a - b

def multiplicacao(a, b):
    # Multiplica dois números
    return a * b

def divisao(a, b):
    # Divide o primeiro número pelo segundo, tratando divisão por zero
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

def fatorial(n):
    # Calcula o fatorial de um número, tratando números negativos
    if n < 0:
        raise ValueError("Fatorial de número negativo não existe")
    return math.factorial(n)

def potenciacao(a, b):
    # Calcula a potenciação de a elevado a b
    return a ** b
```

## Testes Automatizados com Pytest

Os testes para essa calculadora foram criados usando o framework pytest, que facilita a verificação de várias condições esperadas. Cada função da calculadora tem um teste correspondente no arquivo test_calculadora.py.

Os testes cobrem os seguintes cenários:

- Soma de números positivos e negativos.
- Subtração, multiplicação e divisão, incluindo tratamento de divisão por zero.
- Cálculo correto de fatoriais, com tratamento de entrada de números negativos.
- Potenciação, incluindo casos de números elevados a potências negativas e zero.

## Exemplo de Testes:

```python
def test_soma():
    assert soma(1, 2) == 3
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
```

Para rodar os testes, basta executar o comando pytest no diretório do projeto.

## Como Rodar os Testes

Instale as dependências, se necessário, rodando:

```bash
pip install pytest
```

Execute os testes com o seguinte comando:

```bash
pyteest
```

O pytest irá buscar automaticamente os arquivos de teste no formato test_*.py e rodar todos os testes. Se tudo estiver correto, você verá a saída dos testes sendo executados com sucesso.

## Estrutura do Projeto
O projeto está organizado da seguinte maneira:

```bash
/calculadora
    ├── calculadora.py       # Implementação da calculadora
    └── test_calculadora.py  # Arquivo de testes com pytest
```
