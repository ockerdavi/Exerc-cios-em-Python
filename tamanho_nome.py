
'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal", maior que 6 escreva "Seu nome é muito grande".
'''

nome = input("Escreva seu nome para verificar quantas letras tem: ")
tamanho_nome = len(nome)

if tamanho_nome < 5:
    print('Seu nome tem', tamanho_nome, 'letras.')
    print('Portanto seu nome é curto.') 
elif tamanho_nome < 7:
    print('Seu nome tem', tamanho_nome, 'letras.')
    print('Portanto seu nome é normal.')
else:
    print('Seu nome tem', tamanho_nome, 'letras.')
    print('Portanto seu nome é grande.')