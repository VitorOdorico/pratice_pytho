"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

valor_hora = input("quanto você ganha por hora")
horas_trabalhadas = input("Quantas horas voce trabalha por mes")

salario = valor_hora * horas_trabalhadas

print('seu salario é de: ' + salario)

desc_inss = 0.8
desc_IR = 0.11
desc_sind = 0.05
salario_bruto = salario - desc_inss - desc_IR - desc_sind
print("desconto do IR:" + (salario * desc_IR))
print("desconto de inss" + (salario *desc_inss))
print("desconto do sindicato" + (salario * desc_sind))
print("salario bruto: " + salario_bruto)
