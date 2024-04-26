products = {}
while True:
    product = input("Digite o nome do produto: ")
    if product in products:
            resp = input(f"O produto já existe deseja atualizar esse valor? (s/n): ")
            if resp == "s":
                newValue = float(input("Digite o novo valor: "))
                products[product] = newValue
    
    else:
        value = float(input("Digite o valor do produto: "))
        products[product] = value
    resp = input("Deseja continuar cadastrando? (s/n): ")
    if resp == "n": break
for key, value in products.items():
    print(f"{key} - R${value}")
