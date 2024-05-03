"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem"""

notas = []
num = 0

while num != -1:
    num = float(input(f"Digite a nota. ('-1' para encerrar): "))
    if num != -1:
        notas.append(num)

"""A"""
quant = len(notas)
print(f"A quantidade de valores lidos: {quant}")

"""B"""
print(f"Essa é a lista na ordem que foram informados: {notas}")

"""C"""
notas.reverse()
print(f"Essa é a lista na ordem inversa que foram informados: {notas}")

"""D"""
soma = sum(notas)
print(f"Essa é a soma de todos os valores da lista: {soma}")

"""E"""
avg = soma / len(notas)
print(f"Essa é a média dos valores da lista: {avg}")

"""F"""
AcimaMedia = []
for i in notas: 
    if i > avg:
        AcimaMedia.append(i)
print(f"Os valores acima da média foram: {AcimaMedia}")

"""G"""
AbaixoSete = []
for i in notas:
    if i < 7:
        AbaixoSete.append(i)
print(f"Os valores abaixo de 7 foram: {AbaixoSete}")

"""H"""
print("Programa encerrado")
        


