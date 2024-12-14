import os

peso = int(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))

IMC = (peso/(altura**2))

if (IMC < 18.5):
    print(f'O seu peso está menor do que o ideal para o IMC')

elif (18.5 <= IMC < 25):
    print(f'O seu peso está dentro do ideal para o IMC')

elif (IMC >= 25):
    print(f'O seu peso está acima do ideal para o IMC')
