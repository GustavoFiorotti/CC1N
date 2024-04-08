import math

print("Calcular e exibir o tempo (em horas) de autonomia de uma caixa d’água de um restaurante que consome 1350 litros por hora em média.")

r = float(input("Insira o raio do tanque: "))

h = float(input("Insira a altura do tanque: "))

vol = math.pi * r**2 * h

cons_hora = vol / 1350
print(f"A área do tanque foi de {vol:.2f} litros. O tempo de autonomia da caixa é aproximadante {cons_hora: .2f} horas, ou {cons_hora * 60: .1f} minutos.")