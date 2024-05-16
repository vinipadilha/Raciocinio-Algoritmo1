"""Você foi contratado pelo restaurante Boca Feliz para participar do desenvolvimento de
um pequeno controle de estoque de ingredientes iniciado em Python 3.8. O sistema já
possui desenvolvido um dicionário chamado estoque, no qual consta a lista de
ingredientes com suas respectivas quantidades. Também possui outro dicionário
chamado cardapio, no qual constam todos os ingredientes que compõe cada produto
servido no restaurante. Tais estruturas são mostradas a seguir:
estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
Sua primeira tarefa de programador consiste em desenvolver as seguintes
funcionalidades do sistema:
- Imprimir o cardápio do restaurante com as opções de produtos ofertados;
- Logo abaixo do cardápio, exibir a mensagem “O que deseja pedir (0 para sair)?”;
- Digitando “0” deve sair do programa;
- Digitando o nome do produto pode ter uma das seguintes possibilidades:
- Se o item não consta no cardápio exibir a mensagem “Item não localizado no
cardápio”;
- Se não tiver os ingredientes para o preparo do produto em estoque mostrar uma
mensagem para cada ingrediente faltante “Infelizmente acabou o {ingrediente}”;
- Se for possível produzir o produto, reduzir as quantidades de estoque e mostrar a
mensagem “um {produto} saindo no capricho!!!”;
- O programa deve continuar fazendo os pedidos até que o usuário decida sair do
mesmo.
O restaurante Boca Feliz conta com você!!!
"""

estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
while True:
    print("(:Cardápio(:")
    for item in cardapio:
        print(f"{item}: {', '.join(cardapio[item])}")
    print("================")
    print("O que deseja pedir (0 para sair)?")
    pedido = input().strip()
    if pedido == '0':
        print("Até logo!")
        break
    if pedido not in cardapio:
        print("Item não localizado no cardápio")
        continue
    ingredientes_faltando = []
    for ingrediente in cardapio[pedido]:
        if ingrediente not in estoque or estoque[ingrediente] <= 0:
            ingredientes_faltando.append(ingrediente)
    if ingredientes_faltando:
        for ingrediente in ingredientes_faltando:
            print(f"Infelizmente acabou o {ingrediente}")
    else:
        for ingrediente in cardapio[pedido]:
            estoque[ingrediente] -= 1
        print(f"Um {pedido} saindo no capricho!!!")

        













