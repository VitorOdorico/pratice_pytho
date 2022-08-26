# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

from fileinput import hook_compressed


horaTrabalhadas = input("Quantas horas trabalhadas ")
valorHora = input("Valor da sua hora trabalhada: ")


calc = horaTrabalhadas * valorHora

print("seu salario eh de: " + calc)