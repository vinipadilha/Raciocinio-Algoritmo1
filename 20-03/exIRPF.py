renda = float(input("Qual a sua renda mensal? (Ex: 12000)"))
dependentes = float(input("Quantos dependentes você tem? (Ex: 3)"))
pensao = float(input("Você paga pensão? Se sim, quanto? (Ex: 2000) (Se não, colocar '0')"))
deducoes = float(input("Você tem outras deduções? Se sim, qual valor você paga? (Se não, colocar '0')"))
deducaoPorDependente = 189.59
base = renda - ((deducaoPorDependente * dependentes) + pensao + deducoes)
imposto = 0

if base <= 1903.98:
    imposto = 0
    faixa = 1
elif 1903.99 <= base <= 2826.65:
    imposto = (base - 1903.98) * 0.075
    faixa = 2
elif 2826.66 <= base <= 3751.05:
    imposto = (base - 2826.65) * 0.15
    faixa = 3
elif 3751.06 <= base <= 4664.68:
    imposto = (base - 3751.05) * 0.225
    faixa = 4
else:
    imposto = (base - 4664.68) * 0.275
    faixa = 5

    pagar = base * imposto
    
    print(f"O valor do imposto a ser pago é R${pagar:.2f}")
    print(f"Sua faixa é a {faixa}")
    print(f"A taxa aplicada é de {imposto * 100:.1f}%")







