
'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

hora_str = input('Digite seu horário. Ex: 10')
hora_int = int(hora_str)

if hora_int < 12:
    print('Bom dia')
elif hora_int < 18:
    print('Boa tarde')
else: 
    print('Boa noite')
