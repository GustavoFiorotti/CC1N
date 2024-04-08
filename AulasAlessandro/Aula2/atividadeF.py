import math

print("Calcular e exibir o volume em litros de uma esfera de Raio (R), sabendo que o usuário deve informar o Raio (R) em metros.")

raio = float(input("Insira aqui o raio em METROS: "))

print()

print(f"O volume deu{4/3 * math.pi * (raio ** 3): .2f} litros")