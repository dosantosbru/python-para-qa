import os

Atividade_A = int(input("Informe os dias para a atividade A: "))
Atividade_B = int(input("Informe os dias para a atividade B: "))
Atividade_C = int(input("Informe os dias para a atividade C: "))


tempo_total = (Atividade_A + Atividade_B + Atividade_C)


if Atividade_A < 0 or Atividade_B < 0 or Atividade_C < 0:
    print('informe um valor de dias válido')
else:
    print(f'O tempo total do projeto é de {tempo_total}')
