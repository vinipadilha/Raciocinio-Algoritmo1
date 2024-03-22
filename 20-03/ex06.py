op = input("Qual a operação que deseja fazer? 1 para soma, 2 para divisão, 3 para subtração e 4 para multiplicação")
num1 = int(input("Qual o primeiro número: "))
num2 = int(input("Qual o segundo número: "))

if op == 1:
    print(f"{num1} + {num2} = {num1 + num2}")

elif op == 2:
    print(f"{num1} / {num2} = {num1 / num2}")

elif op == 3:
    print(f"{num1} - {num2} = {num1 - num2}")

elif op == 4:
    print(f"{num1} * {num2} = {num1 * num2}")
else: 
    print("Digite um valor válido")

