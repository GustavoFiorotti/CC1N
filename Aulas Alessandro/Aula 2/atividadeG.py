import math

print("Calcular e exibir quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.")

ganha = float(input("Insira aqui o quanto você ganha por hora: "))

horas = float(input("Insira aqui quantas horas você trabalha por mês: "))

bruto = ganha * horas

inss= bruto * 0.08

print()

print(f"Com você ganhando R${ganha} em {horas:.0f} horas por mês, seu salário bruto é R${bruto}\n-R${inss} de INSS")


imposto = bruto * 0.11

print(f"-R${imposto} de imposto de renda")

sindi = bruto * 0.05

liquido = bruto - inss - sindi - imposto
print(f"-R${sindi} do sindicato\n\nAo todo, foi descontado R${bruto - liquido} e por fim, o salário líquido ficou de R${liquido}")