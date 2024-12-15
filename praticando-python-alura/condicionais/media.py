"""Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados,
ficaram de recuperação ou reprovados. 
As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. 
Com base na média, exiba a situação do aluno."""

Nota_periodo1 = int(input("Informe a primeira nota: "))
Nota_periodo2 = int(input("Informe a segunda nota: "))
Nota_periodo3 = int(input("Informe a terceira nota: "))

media = (Nota_periodo1 + Nota_periodo2 + Nota_periodo3) / 3

if media >= 7:
    print(f'O aluno está aprovado')
elif 5 <= media < 7:
    print(f'O aluno está de recuperação')
else:
    print(f'O aluno está reprovado')
