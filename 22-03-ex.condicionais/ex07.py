dia = int(input("Insira seu dia de nascimento. (Ex: 15): "))
mes = int(input("Insira seu mês de nascimento. (Ex: 06): "))
ano = int(input("Insira seu ano de nascimento. (Ex: 2001): "))
modo = [
    "'1' para Data simples. Ex.: 10/08/1990",
    "'2' para Data abreviada. Ex.: 10/ago/1990",
    "'3' para Data completa. Ex.: 10 de agosto de 1990"
]

print(modo)

formato = int(input("Digite o número que deseja para exibição da data: "))

if formato == 1:
    print(f"{dia}/{mes}/{ano}")
elif formato == 2:
    mesesAbreviados = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    print(f"{dia}/{mesesAbreviados[mes - 1]}/{ano}")
elif formato == 3:
    mesesCompletos = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    print(f"{dia} de {mesesCompletos[mes - 1]} de {ano}")
else:
    print("Você deve digitar 1, 2 ou 3")