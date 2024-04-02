import math

print("Faça um programa que peça o tamanho de um arquivo para download (em Megabytes) e a velocidade de um link de Internet (em Megabytes / Segundo), calcule e informe o tempo: Minutos + Segundos aproximado de download do arquivo usando este link.")

tamanho = float(input("Insira o tamanho do arquivo em MEGABYTES: "))

velocidade = float(input("Digite a velocidade da internet: "))

tempo_segundo = tamanho / velocidade

print()

print(f"Tempo aproximado de download: {tempo_segundo // 60} minutos e {tempo_segundo % 60} segundos.")