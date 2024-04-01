import math

print("Calcular e exibir a distância máxima (em Quilômetros) de autonomia de um carro que possui um tanque de combustível cúbico de lado (L) em metros e Altura (h) de preenchimento do tanque. Sabendo que seu consumo é em média 10 km/litro. Sabendo que 1 m3 = 1000 Litros.")

L = float(input("Insira a largura do tanque: "))

A = float(input("Insira a altura do tanque: "))

autonomia = L * L * A * 1000


print()

print(f"A quilometragem máxima deste carro é {autonomia / 10}Km.")
