print("Código para calcular a média do semestre.")

print()

while True:
    b1 = float(input("Escreva a nota do primeiro bimestre: "))
    
    b2 = float(input("Escreva a nota do segundo bimestre: "))
    if b1 > 10 or b2 > 10:
        print(f"ERRO, você inseriu uma nota maior que o possível.")
        continue
    break

sem = (b1 + b2) / 2

if sem >= 7:
    print(f"Você PASSOU com uma média de {sem}.")

elif sem < 3:
    print(f"Sua nota foi {sem}, por ser menor que 3 você está REPROVADO.")

elif 3 <= sem < 7:
    rec = float(input(f"Sua média atual é {sem} e você ficou de RECUPERAÇÃO, qual a sua nota da prova de recuperação? "))
    sem = (sem + rec) / 2
    if sem >= 5:
        print(f"Sua nota foi {sem}, você PASSOU de semestre.")
    elif sem < 5:
        print(f"Sua nota foi {sem}, por ser menor que 5 você foi REPROVADO.")
