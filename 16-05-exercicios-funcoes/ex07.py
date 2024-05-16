"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de
uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar
estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa
que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá
voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a
prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade
e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para
pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de
juros por dia de atraso."""

def valorPagamento():
    prestacoes = 0
    valorPrestacoes = 0

    while True:
        valor = int(input("Digite aqui o valor da prestação (0 para encerrar): "))
        dias = int(input("Quantos dias está atrasada? Digite aqui: "))

        if valor == 0:
            print("Seu programa foi encerrado")
            break

        else: 
            pagar = valor + (valor * 0.03) + (0.01 * dias)
            print(f"O valor a ser pago é R$ {pagar}")
            prestacoes += 1
            valorPrestacoes += pagar

    return prestacoes, valorPrestacoes

prestacoes, valorPrestacoes = valorPagamento()

print(f"{prestacoes} foram feitas")
print(f"R$ {valorPrestacoes}  valor pago em prestações")









