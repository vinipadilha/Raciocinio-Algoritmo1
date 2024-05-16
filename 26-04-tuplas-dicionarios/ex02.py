"""Como navegador de uma nave interestelar da frota Alfa, uma de suas principais funções
á calcular as distâncias no espaço. Para isto, realizar rapidamente conversão de unidades
de tempo é uma habilidade fundamental em seu trabalho. Assim sendo, a fim de facilitar
seu próprio trabalho, você, programador em linguagem Python, decide desenvol ver seu
próprio conversor unidades de tempo em deslocamento no espaço. Para tanto,
consegue as seguintes informações de base para seu programa: um dicionário chamado
anos_luz, que tem os valores das demais unidades de tempo convertidos para valor em
anos luz, e uma lista chamada unidades com o nome e abreviações das unidades de
tempo, como segue:
ano_luz = {
"pc": 0.31,
"al": 1,
"ae": 63241.09,
"ml": 525960.23,
"sl": 31557609.92
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz
(ml)", "Segundo-Luz (sl)"]
Desta forma, sua tarefa é desenvolver um programa com as seguintes funcionalidades:
- Imprimir a lista de unidades de conversão
- Solicitar o valor que se deseja converter usando a frase “Valor a ser convertido: ”
- Solicitar a unidade origem do valor usando a frase “Converter de: ”
- Solicitar a unidade destino de conversão usando a franse “Converter para: ”
- Exibir o valor convertido com a frase “Conversão: {valor} {unidade origem} = {valor}
{unidade destino}”
A frota Alfa conta com você, oficial navegador!!!
"""

anos_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557600.0  
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]
print("Lista de unidades de conversão:")
for i, unidade in enumerate(unidades):
    print(f"{i + 1}. {unidade}")
valor = float(input("Valor a ser convertido: "))
print("Escolha a unidade de origem:")
for i, unidade in enumerate(unidades):
    print(f"{i + 1}. {unidade}")
origem_index = int(input("Converter de (digite o número correspondente): ")) - 1
origem = unidades[origem_index].split("(")[1].split(")")[0]
print("Escolha a unidade de destino:")
for i, unidade in enumerate(unidades):
    print(f"{i + 1}. {unidade}")
destino_index = int(input("Converter para (digite o número correspondente): ")) - 1
destino = unidades[destino_index].split("(")[1].split(")")[0]
valor_convertido = valor * anos_luz[origem] / anos_luz[destino]
print(f"Conversão: {valor} {origem} = {valor_convertido} {destino}")
















