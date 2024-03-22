salario = float(input("Digite seu sálario aqui: "))

if salario > 5000:
    abono = salario * 0.15
else:
    abono = salario * 0.10

print(f"O valor do seu abono de final de ano é R${abono:.2f}.")