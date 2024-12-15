"""Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente."""


Distancia = int(input("Informe a distância percorrida: "))

if Distancia <= 100:
    print("O valor do pedágio é de R$ 10,00")
elif Distancia <= 200:
    print("O valor do pedágio é de R$ 20,00")
else:
    print("O valor do pedágio é de R$ 30,00")
