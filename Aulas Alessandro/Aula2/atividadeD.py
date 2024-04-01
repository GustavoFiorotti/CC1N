import math

print("Calcular e exibir a área e o comprimento de um círculo de Raio (R), sabendo que, Area = π * R 2 e Comprimento = 2 * π * R.")

raio = float(input("Insira o raio do círculo: "))

print()

print(F"A área do círculo é {math.pi * (raio ** 2): .2f} e o comprimento é {2 * math.pi * raio: .2f}")