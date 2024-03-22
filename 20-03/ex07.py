lado1 = int(input("Digite o lado da primeira aresta: "))
lado2 = int(input("Digite o lado da segundo aresta: "))
lado3 = int(input("Digite o lado da terceiro aresta: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("Seu trinângulo é equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Seu triângulo é isóceles")
    else:
        print("Seu triângulo é escaleno")
else: 
    print("Digite valores válidos")