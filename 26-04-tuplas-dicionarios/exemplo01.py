people = []
while True:
    name = input(f"Digite o nome: ")
    rg = input(f"Digite o RG: ")
    cpf = (f"Digite o CPF: ")
    person = (name, rg, cpf)
    people.append(person)
    resp = input("Deseja continuar cadastrando? (s/n): ")
    if resp == 'n': break
print(f"lista de pessoas: {people}")
for person in people:
    print(f"Nome: {person[0]}")
    print(f"RG: {person[1]}")
    print(f"CPF: {person[2]}")
    print("==============")
