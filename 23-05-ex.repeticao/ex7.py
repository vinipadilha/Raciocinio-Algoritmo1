#Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
#parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
#conjunto de palavras.
contagemA = 0

while True:
    p = input("Digite a palavra que deseja (ou pressione Enter para sair): ")

    if p == "": 
        break

    else:
        contagemA += p.lower().count('a')

print("O número total de letras 'A' é:", contagemA)




