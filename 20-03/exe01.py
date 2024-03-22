grade1 = float(input("Digite a note do 1 bimestre: "))
grade2 = float(input("Digite a note do 2 bimestre: "))
grade3 = float(input("Digite a note do 3 bimestre: "))
grade4 = float(input("Digite a note do 4 bimestre: "))
avg = (grade1 + grade2 + grade3 + grade4) / 4

print(f"A média da disciplina é {avg:.1f}")

if avg >= 7:
    print("Você está aprovado")

else:
    print("Se deu mal")




