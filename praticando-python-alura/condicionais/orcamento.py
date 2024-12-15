""" Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000, 00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento."""


import locale
from decimal import Decimal

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

limite = Decimal('3000.00')
entrada = input(
    "Digite o valor de despesas realizadas em reais (exemplo: 2.999,99): ")
total_despesas = Decimal(entrada.replace('.', '').replace(',', '.'))

if total_despesas <= limite:
    print(
        f'Você está dentro do limite de gastos. Seu gasto foi de {locale.currency(total_despesas, grouping=True)}.')
else:
    print(
        f'Você ultrapassou o limite de gastos. Seu gasto foi de {locale.currency(total_despesas, grouping=True)}.')
