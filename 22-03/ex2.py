# CALCULADORA IMC 
peso = int(input("Qual seu peso? (Ex: 60): "))
alt = float(input("Qual sua peso? (Ex: 1.70): "))

result = peso / (alt **2)
print(f"O seu IMC é {result:.1f}")

if result < abPeso:
    print("Você está abaixo do peso")
elif result < pesoN:
    print("Você está com peso normal")
elif result < AcPeso:
    print("Você está acima do peso")
else:
    print("Você está obeso")

abPeso = 18.5
pesoN = 25
AcPeso = 30

