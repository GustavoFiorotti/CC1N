import math

print("Calcular e exibir o IMC (Índice de Massa Corpórea) de uma pessoa de altura (H) em metros e massa(M) em quilogramas.")

peso = float(input("Insira aqui o seu peso (KG): "))

altura = float(input("Insira agora a altura(em metros):"))

print()

print(f"O seu IMC deu {peso / altura**2: .2f}")