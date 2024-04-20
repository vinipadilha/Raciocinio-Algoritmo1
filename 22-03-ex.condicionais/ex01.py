#LISTAS DE EXERCICIOS CONDICIONAIS
sex = float(input("Digite '1' se você é homem e '2' para mulher: "))
alt = float(input("Digite sua altura. (Ex: 1.70): "))

if sex == 1:
    peso = (72.7 * alt) - 58
elif sex == 2: 
    peso = (62.1 * alt) - 44.7
else: 
    print("Digite um número válido")

print(f"Seu peso ideal é: {peso:.1f}KG")
