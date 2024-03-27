#CPF 
cpf1 = int(input('Digite o primeiro dígito do seu cpf: '))
cpf2 = int(input('Digite o segundo dígito do seu cpf: '))
cpf3 = int(input('Digite o terceiro dígito do seu cpf: '))
cpf4 = int(input('Digite o quarto dígito do seu cpf: '))
cpf5 = int(input('Digite o quinto dígito do seu cpf: '))
cpf6 = int(input('Digite o sexto dígito do seu cpf: '))
cpf7 = int(input('Digite o sétimo dígito do seu cpf: '))
cpf8 = int(input('Digite o oitavo dígito do seu cpf: '))
cpf9 = int(input('Digite o nono dígito do seu cpf: '))
cpf10 = int(input('Digite o décimo dígito do seu cpf: '))
cpf11 = int(input('Digite o décimo primeiro dígito do seu cpf: '))
#validação primeiro dígito

resul1 = (cpf1 * 10) + (cpf2 * 9) + (cpf3 * 8) + (cpf4 * 7) + (cpf5 * 6) + (cpf6 * 5) + (cpf7 * 4) + (cpf8 * 3) + (cpf9 * 2)
sobra1 = (resul1 * 10) % 11

primeiroDigitoVerif = cpf10

if sobra1 == 10:
    resultado = 0

if sobra1 == primeiroDigitoVerif:
    print("A primeira parte da validação está correta.")
else:
    print("A primeira parte da validação não está correta!")

#Validação segundo dígito
resul2 = (cpf1 * 11) + (cpf2 * 10) + (cpf3 * 9) + (cpf4 * 8) + (cpf5 * 7) + (cpf6 * 6) + (cpf7 * 5) + (cpf8 * 4) + (cpf9 * 3) + (cpf10 * 2)
sobra2 = (resul2 * 10) % 11

segundoDigitoVerif = cpf11
if sobra2 == 10:
    resultado = 0

if sobra2 == segundoDigitoVerif:
    print("A segunda parte da validação está correta.")
else:
    print("A segunda parte da validação não está correta!")
