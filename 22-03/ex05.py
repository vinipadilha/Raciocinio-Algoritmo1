desti = int(input("Qual sua região de destino? 1 para Norte, 2 para Nordeste, 3 para Centro-Oeste, 4 para Sul: "))
idaVolta = input("A viagem é ida e volta? (S/N): ")

if desti == 1:
    if idaVolta.upper() == "S":
        print(f"O preço da passagem ida e volta é R$ 900,00")
    else:
        print(f"O preço da passagem ida é R$ 500,00")

elif desti == 2:
    if idaVolta.upper() == "S":
        print(f"O preço da passagem ida e volta é R$ 650,00")
    else:
        print(f"O preço da passagem ida é R$ 350,00")

elif desti == 3:
    if idaVolta.upper() == "S":
        print(f"O preço da passagem ida e volta é R$ 600,00")
    else:
        print(f"O preço da passagem ida é R$ 350,00")

elif desti == 4:
    if idaVolta.upper() == "S":
        print(f"O preço da passagem ida e volta é R$ 550,00")
    else:
        print(f"O preço da passagem ida é R$ 300,00")








