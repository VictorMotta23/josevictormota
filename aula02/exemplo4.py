#leia dois números inteiros e mostre somente o menor valor
num1 = int(input("informe o 1º número inteiro:"))
num2 = int(input("informe o 2º número inteiro:"))

if num1<num2:
    print("O menor valor informado é:",num1)
elif num1==num2:
    print("Você digitou valores iguais! =(")
else:
    print("O menor valor informado é:",num2)  