import math

print("Calcular e exibir a quantidade de tinta (em latas) e o custo (em reais) para pintar um tanque cilíndrico de base circular de Raio (R) e altura (H) em metrosM")

r = float(input("Insira o raio do tanque cilíndrico: "))

h = float(input("Insira a altura do tanque cilíndrico: "))

vol = math.pi * r**2 * h

vol_lata = vol / 3

lata = vol_lata / 5

custo = lata * 50
print()

print(f"A área do tanque foi de {vol:.2f} litros, sendo usados {vol_lata:.2f} litros de tinta, dando aproximadamente {int(lata)} latas de tinta. O custo disso daria R${custo: .2f}.")