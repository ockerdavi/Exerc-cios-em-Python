"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é parou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

numero_str = input('Digite um numero inteiro: ')

try:

    print(numero_str.isdigit())   

    numero_float = int(numero_str)

    if numero_float % 2 == 0:
        print(f'O numero {numero_float} é par')
    else:
        print(f'{numero_float} é ímpar')
except:
    print('Digite apenas numeros inteiros.')
