#Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
#porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer

p = int(input("Quantos pontos devem ser feitos para vencer: "))

p1 = 0
p2 = 0

while True:
    player1 = int(input("Jogador 1: Digite 1 para pedra, 2 para tesoura ou 3 para papel: "))
    player2 = int(input("Jogador 2: Digite 1 para pedra, 2 para tesoura ou 3 para papel: "))

    if player1 == player2:
        print("Rodada empatada, ninguém marcou pontos.")
    elif player1 == 1 and player2 == 2: 
        print("Rodada vencida por Jogador 1.")
        p1 += 1
    elif player1 == 1 and player2 == 3:
        print("Rodada vencida por Jogador 2.")
        p2 += 1
    elif player1 == 2 and player2 == 3:
        print("Rodada vencida por Jogador 1.")
        p1 += 1
    elif player1 == 2 and player2 == 1:
        print("Rodada vencida por Jogador 2.")
        p2 += 1
    elif player1 == 3 and player2 == 2:
        print("Rodada vencida por Jogador 2.")
        p2 += 1
    elif player1 == 3 and player2 == 1:
        print("Rodada vencida por Jogador 1.")
        p1 += 1

    print(f"Pontuação - Jogador 1: {p1}, Jogador 2: {p2}")

    if p1 == p:
        print("Jogador 1 venceu o jogo!")
        break
    elif p2 == p:
        print("Jogador 2 venceu o jogo!")
        break

print("Jogo encerrado.")