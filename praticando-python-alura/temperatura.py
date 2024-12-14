
entrada = input('Informe a temperatura ambiente:')

if entrada.isnumeric():
    temperatura_ambiente = int(entrada)
    temperatura_esperada = 25

    if temperatura_ambiente > temperatura_esperada:
        print(
            f'ALERTA! {temperatura_ambiente} Temperatura acima do limite permitido')
    elif temperatura_ambiente < 0:
        print(f'Informe uma temperatura válida')
    else:
        print(f'{temperatura_ambiente} dentro do limite permitido')
else:
    print('Por favor, insira um valor numérico válido.')
