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

def calcularPercentual(votos, totalVotos):
    return (votos / totalVotos) * 100

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("As possíveis respostas são:")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")


def resposta():
    votos = [0, 0, 0, 0, 0, 0]
    totalVotos = 0  
    voto = int(input("Digite a opção escolhida (de 1 a 6, ou 0 para encerrar): "))
    
    while voto != 0:
        if 1 <= voto <= 6:
            votos[voto - 1] += 1 
            totalVotos += 1
            print("Voto computado para a opção", voto)
        else:
            print("Digite um valor válido (de 1 a 6).")
        voto = int(input("Digite a opção escolhida (de 1 a 6, ou 0 para encerrar): "))
    
    print("\nSistema Operacional    Votos      %")
    print("===================    =====     ======")
    print(f"Windows Server:          {votos[0]}       {calcularPercentual(votos[0], totalVotos):.1f}%")
    print(f"Unix:                    {votos[1]}       {calcularPercentual(votos[1], totalVotos):.1f}%")
    print(f"Linux:                   {votos[2]}       {calcularPercentual(votos[2], totalVotos):.1f}%")
    print(f"Netware:                 {votos[3]}       {calcularPercentual(votos[3], totalVotos):.1f}%")
    print(f"Mac OS:                  {votos[4]}       {calcularPercentual(votos[4], totalVotos):.1f}%")
    print(f"Outro:                   {votos[5]}       {calcularPercentual(votos[5], totalVotos):.1f}%")
    print("===================    =====")
    print(f"Total                    {totalVotos}")

resposta()



