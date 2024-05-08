"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O
programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme
o exemplo abaixo

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado final:

"""
while True:
    nome = input("Digite o nome do atleta: ")

    if nome == "":
        print("O programa foi encerrado.")
        break

    s1 = float(input("Digite a distância do 1º salto: "))
    s2 = float(input("Digite a distância do 2º salto: "))
    s3 = float(input("Digite a distância do 3º salto: "))
    s4 = float(input("Digite a distância do 4º salto: "))
    s5 = float(input("Digite a distância do 5º salto: "))
    media = (s1 + s2 + s3 + s4 + s5) / 5
        
    print(f"Atleta: {nome}")
    print(f"Primeiro salto: {s1} m")
    print(f"Segunda salto: {s2} m")
    print(f"Terceiro salto: {s3} m")
    print(f"Quarto salto: {s4} m")
    print(f"Quinto salto: {s5} m")
    print("\nResultado final abaixo\n")
    print(f"Média dos saltos: {media} m\n")



