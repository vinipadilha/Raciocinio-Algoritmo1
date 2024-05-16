"""Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
carros faz com um litro de combustível. Calcule e mostre:
a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de
1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue
uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os
dados são fictícios e podem mudar a cada execução do programa."""

carros = []
consumo = []
milkm = []
valor = []

print("Relatorio final")

for i in range(5):
    carro = input(f"Digite o nome do {i + 1} carro: ")
    combust = float(input(f"Digite o consumo do {i + 1} carro (km/l): "))
    qnt = 1000 / combust 
    din = qnt * 2.25

    carros.append(carro)
    consumo.append(combust)
    milkm.append(qnt)
    valor.append(din)
    print(f"Veículo {i + 1}")
    print(f"Nome: {carro}")
    print(f"Km/L: {combust}")

print("Relatório final")
print(f"1 - {carros[0]} - {consumo[0]:.1f} - {milkm[0]:.1f} L - R$ {valor[0]:.2f}")
print(f"2 - {carros[1]} - {consumo[1]:.1f} - {milkm[1]:.1f} L - R$ {valor[1]:.2f}")
print(f"3 - {carros[2]} - {consumo[2]:.1f} - {milkm[2]:.1f} L - R$ {valor[2]:.2f}")
print(f"4 - {carros[3]} - {consumo[3]:.1f} - {milkm[3]:.1f} L - R$ {valor[3]:.2f}")
print(f"5 - {carros[4]} - {consumo[4]:.1f} - {milkm[4]:.1f} L - R$ {valor[4]:.2f}")



