valor = float(input("Qual o valor do produto? "))
condi = float(input("Qual seria a forma de pagamento? 1 para dinheiro/cheque, 2 para cartão de crédito, 3 em duas vezes no cartão -> "))

if condi == 1:
    pagar = valor - (valor * 0.1)

elif condi == 2:
    pagar = valor - (valor * 0.15)

elif condi == 3 and valor > 200:
    pagar = valor 

elif condi == 3 and valor < 200:
    pagar = valor + (valor * 0.10)

print(f"Seu valor a pagar será R$ {pagar:.2f}")
    