"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não
deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das
opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa
deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída
foi dado pela empresa, e é o seguinte"""

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("As possíveis respostas são:")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")


def respota():
    voto = int(input("Digite a opção escolhida: "))
    if 1 <= voto <= 6:
        print("Você escolheu a opção", voto)
    elif voto == 0:
        print("O programa foi encerrado.")
    else:
        print("Digite um valor válido (de 0 a 6).")
        return resposta