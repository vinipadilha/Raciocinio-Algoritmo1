palpite1 = int(input("Jogador 1, faça seu palpite (1 para par e 2 para ímpar): "))
num1 = int(input("Jogador 1, escolha um número entre 1 e 5: "))
palpite2 = int(input("Jogador 2, faça seu palpite (1 para par e 2 para ímpar): "))
num2 = int(input("Jogador 2, escolha um número entre 1 e 5: "))     

if num1 < 1 or num1 > 5 or num2 < 1 or num2 > 5:
    print("A rodada foi cancelada, rode novamente")

else: 
    soma = num1 + num2
    result = soma % 2

    if result == 0 and palpite1 == 1 or result != 0 and palpite1 == 2:
        print("O jogador 1 ganhou essa rodada!")
    elif result == 0 and palpite2 == 1 or result != 0 and palpite2 == 2:
        print("O jogador 2 ganhou essa rodada!")
    else: 
        print("Ninguém ganhou essa rodada!")
        