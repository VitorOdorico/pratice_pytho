# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

peso = input("De o valor do peso")
altura = input("Qual a sua altura")
genero = input["masculino", "feminino"]


calculo_peso = ((peso*altura) -58)
peso_ideal = calculo_peso == ((72.7*altura) -58)

if calculo_peso == peso_ideal:
    print("Voce esta dentro do seu peso ideal")