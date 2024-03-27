renda = float(input("Qual a sua renda mensal? (Ex: 12000): R$ "))
dependentes = float(input("Quantos dependentes você tem? (Ex: 3): "))
pensao = float(input("Você paga pensão? Se sim, quanto? (Ex: 2000) (Se não, colocar '0'): "))
deducoes = float(input("Você tem outras deduções? Se sim, qual valor você paga? (Se não, colocar '0'): "))
deducaoPorDependente = 189.59
base = renda - ((deducaoPorDependente * dependentes) + pensao + deducoes)
imposto = 0
faixa1 = 1903.98
feixa2 = 2826.65
faixa3 = 3751.05
faixa4 = 4664.68
fc2 = (faixa2 - faixa1) * 0.075
fc3 = fc2 + (faixa3 - faixa2) * 0.15
fc4 = fc3 + (faixa4 - faixa3) * 0.225

if base <= faixa1:
    imposto = 0
    faixa = 1
elif base <= faixa2:
    imposto = (base - faixa1) * 0.075
    faixa = 2
elif base <= faixa3:
    imposto = (base - faixa2) * 0.15 + fc2
    faixa = 3
elif base <= faixa4:
    imposto = (base - faixa3) * 0.225 + fc3
    faixa = 4
else:
    imposto = (base - faixa4) * 0.275 + fc4

ae = imposto / base * 100
faixa = 5

pagar = imposto

print(f"O valor do imposto a ser pago é R${pagar:.2f}")
print(f"Sua faixa é a {faixa}")
print(f"A alíquota que se enquadra este IRPF é {ae:.1f}%")
print(f"A taxa aplicada é de {imposto * 100:.1f}%")
