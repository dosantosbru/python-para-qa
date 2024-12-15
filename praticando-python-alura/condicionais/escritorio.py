""""
    Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar.
    Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. 
    Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.
"""

from datetime import datetime, time

inicio = time(8, 0)
fim = time(18, 0)

minutos = input("Informe os minutos atuais: ")

hora = input("Informe o horário atual: ")
if hora.isnumeric() and minutos.isnumeric():
    horario_informado = f'{hora}h{minutos}'
    horario_formatado = horario_informado.replace('h', ':')
horario = datetime.strptime(horario_formatado, "%H:%M").time()

if inicio <= horario <= fim:
    print(f'Acesso permitido {horario_formatado}')
else:
    print(f'Acesso negado {horario_formatado}')
