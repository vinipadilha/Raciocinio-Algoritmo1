'''
ex 9
Reverso do número. Faça uma função que retorne o reverso de um número
inteiro informado. Por exemplo: 127-> 721'''

numero = input("Digite um número")
def inverter(numstr):
    return numstr[::-1]
print(inverter(numero))