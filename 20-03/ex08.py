
nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

avg = (nota1 + nota2 + nota3 + nota4) / 4

aulasTootais = 40
presenca = ((aulasTotais - faltas) / aulasTotais) * 100

if avg >= 7 and presenca >= 75:
    print("O aluno foi aprovado!")
elif avg < 7:
    print("O aluno foi reprovado devido à média abaixo de 7.")
else:
    print("O aluno foi reprovado devido à frequência abaixo de 75%.")



