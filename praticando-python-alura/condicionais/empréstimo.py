"""Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima."""


import locale

# Configurar para o formato de moeda brasileira R$
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def converter_para_float(valor):
    valor = valor.replace('.', '').replace(',', '.')
    return float(valor)


renda = input("Informe sua renda mensal (ex.: 3.000,00): ")
parcelas = input("Informe o valor da parcela que deseja pagar (ex.: 900,00): ")


renda = converter_para_float(renda)
parcelas = converter_para_float(parcelas)


if renda > 2000 and parcelas <= 0.3 * renda:
    print(
        f"Empréstimo aprovado!  : {locale.currency(renda)}, Parcela: {locale.currency(parcelas)}")
else:
    print(
        f"Empréstimo negado. Renda de {locale.currency(renda)} com parcela de {locale.currency(parcelas)} ultrapassa 30% da renda.")
a