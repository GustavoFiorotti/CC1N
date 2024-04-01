import math

print("Calcular e exibir a distância entre dois pontos quaisquer do plano, P(x1 , y1) e Q(x2 , y2)")

x1, y1 = map(int,input("Insira as coordenadas de P(ex.: 1,2): ").split(","))

x2, y2 = map(int,input("Insira as coordenadas de Q: ").split(","))

print(f"Sendo P{x1,y1} e Q{x2,y2}, a distância é: {math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2):.2f}")