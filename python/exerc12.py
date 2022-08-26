# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

peso = input("De o valor do peso")
altura = input("Qual a sua altura")

calculo_peso = ((peso*altura) -58)
peso_ideal = calculo_peso == ((72.7*altura) -58)

if calculo_peso == peso_ideal:
    print("Voce esta dentro do seu peso ideal")