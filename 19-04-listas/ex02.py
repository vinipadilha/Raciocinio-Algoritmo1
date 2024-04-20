list1 = []
list2 = []
list3 = []
for i in range(5):
    e = input(f"Digite o {i + 1}º elemento da lista 1: ")
    list1.append(e)

for i in range(5):
    e = input(f"Digite o {i + 1}º elemento da lista 2: ")
    list2.append(e)

for i in range(5):
    e = input(f"Digite o {i + 1}º elemento da lista 3: ")
    list3.append(list1[i])
    list3.append(list2[i])
print(list3)
