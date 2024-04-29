"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada"""
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

for i in range(10):
    num1 = float(input(f"Digite o {i + 1}º número: "))
    vetor1.append(num1)

    
for i in range(10):
    num2 = float(input(f"Digite o {i + 1}º número: "))
    vetor2.append(num2)

for i in range(10):
    num3 = float(input(f"Digite o {i + 1}º número: "))
    vetor3.append(num3)

for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i]) 
    vetor4.append(vetor3[i]) 

linha = print(f"===============================================")

print(f"Esse é o 1º vetor: {vetor1}")
print(linha)
print(f"Esse é o 2º vetor: {vetor2}")
print(linha)
print(f"Esse é o 3º vetor: {vetor3}")
print(linha)
print(f"E assim ficou os vetores intercalados: {vetor4}")
