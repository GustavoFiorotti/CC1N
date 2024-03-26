print ("Hello World")

print ( )

numero = 5.24362

print("Numero qualquer:",numero)

print(f"Numero qualquer:{numero: .1f}")

#.upper() e .lower() para transformar a saída em caixa alta e baixa, respectivamente.
numero = (input("Insira um número qualquer: ")).upper()
verdade = (input(f"Você digitou o número {numero}, verdade?: ")).upper()
if verdade == "V":
    print(f"Então é verdade, você digitou o número {numero}.")
elif verdade == "F":
    print(f"Então você não digitou {numero}")
