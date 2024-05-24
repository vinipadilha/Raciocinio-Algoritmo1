m = float(input("Digite a massa do material radioativo (em gramas): "))

tempo = 0

while True:
    if m <= 0.5:
        break
    else:
        m = m / 2
        tempo += 50

print(f"A massa final é {m:.2f} gramas e foram gastos {tempo} segundos")