"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa
deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma
para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor 'A' para A.M. e 'P' para
P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua
um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar"""        

'''converte de 24 para 12'''
def converterHora(hora, minuto):
    if hora == 0:
        return 12, minuto, 'A'
    elif 1 <= hora < 12:
        return hora, minuto, 'A'
    elif hora == 12:
        return 12, minuto, 'P'
    else:
        return hora - 12, minuto    , 'P'

def mostraHora(hora, minuto, ap):
    if ap == "A":
        apSrc = "A.M."
    else:
        apSrc = "P.M."

    print(f"A hora convertida é: {hora}:{minuto:02d} {apSrc}")

while True:
    hora = int(input("Digite as horas (0-23): "))
    minuto = int(input("Digite os minutos (0-59): "))
    
    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
        print("Por favor, insira valores válidos para horas (0-23) e minutos (0-59).")
        continue
    
    else:
        hora12, minuto12, ap = converterHora(hora, minuto)
        mostraHora(hora12, minuto12, ap)

        repetir = input("Deseja converter outra hora? (s/n): ").lower()  
        if repetir != 's':
            break

