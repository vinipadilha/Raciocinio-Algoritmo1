"""Criar um programa que lê as temperaturas médias de cada mês
do ano e as armazena em uma lista. Usar um outro vetor para
guardar e exibir, quando necessário, os nomes dos meses do ano.
Calcular a média anual de temperatura, e informar quais meses
ficaram acima desta média anual. """


meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
guardar_temp = []
contador = 0

for i in meses:
    temperatura = int(input(f"Digite a temperatura do mês de {i}: "))
    guardar_temp.append(temperatura)

avg = sum(guardar_temp) / 12

avg_acima = []
for a in guardar_temp:
    if a > avg:
        avg_acima.append(meses[contador])
        contador+=1

print(f"os meses acima da média são {avg_acima}")
