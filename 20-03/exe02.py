num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")

if num1 < num2 and num1 < num3:
    menor = num1;

elif num2 < num1 and num2 < num3:
    menor = num2;

else:
    menor = num3;

print(f"o menor número é o: {menor}")

