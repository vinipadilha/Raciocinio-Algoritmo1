"""Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá
receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse
o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação
igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:"""

totalMouses = 0
esfera = 0
limpeza = 0
caboConector = 0
quebrado = 0

while True:
    mouseId = int(input("Digite o número de identificação do mouse (ou 0 para encerrar): "))

    if mouseId == 0:
        break

    print("Tipos de defeito:")
    print("1 - necessita da esfera")
    print("2 - necessita de limpeza")
    print("3 - necessita troca do cabo ou conector")
    print("4 - quebrado ou inutilizado")
    defeito = int(input("Digite o tipo de defeito: "))

    if defeito == 1:
        esfera += 1
    elif defeito == 2:
        limpeza += 1
    elif defeito == 3:
        caboConector += 1
    elif defeito == 4:
        quebrado += 1
    else:
        print("Tipo de defeito inválido. Tente novamente.")
        continue
    totalMouses += 1

    porcentoEsfera = (esfera / totalMouses) * 100
    porcentoLimpeza = (limpeza / totalMouses) * 100
    porcentoCaboConector = (caboConector / totalMouses) * 100
    porcentoQuebrado = (quebrado / totalMouses) * 100


    print(f"Quantidade de mouses: {totalMouses}")
    print(f"Situação                                Quantidade        Percentual")
    print(f"1- necessita da esfera                 {esfera}              {porcentoEsfera:.2f}%")
    print(f"2- necessita de limpeza                {limpeza}              {porcentoLimpeza:.2f}%")
    print(f"3- necessita troca do cabo ou conector {caboConector}              {porcentoCaboConector:.2f}%")
    print(f"4- quebrado ou inutilizado             {quebrado}              {porcentoQuebrado:.2f}%")



