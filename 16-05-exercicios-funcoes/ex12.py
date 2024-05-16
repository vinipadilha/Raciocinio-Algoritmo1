"""Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os
carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou
qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão
devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados."""

import random

palavra = input("Digite uma palavra: ")
def embaralha_palavra(palavra):
    palavra = palavra.lower()
    caracteres = list(palavra)
    random.shuffle(caracteres)
    palavra_embaralhada = ''.join(caracteres)
    return palavra_embaralhada

resultado = embaralha_palavra(palavra)
print("Palavra embaralhada:", resultado)

