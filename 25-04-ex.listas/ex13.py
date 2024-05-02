"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )"""

tempMed = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in meses:
    avg = float(input(f"Digite a temperatura média do mês de {i}: "))
    tempMed.append(avg)

mediaTodos = sum(tempMed) / 12
acimaMedia = []
for i in range(12):
    if tempMed[i] > mediaTodos:
        acimaMedia.append(meses[i])

print(f"Os meses que ficaram acima da média são: {acimaMedia}")



