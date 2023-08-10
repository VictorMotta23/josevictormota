#exemplo da função range()

print(list(range(2,20)))
print(list(range(10)))
print(range(10))
print(list(range(10,100,5)))
print("-"*50)

#Loop for
for i in range(10):
    print(i, end=" ")
print("\nValor final do contador:",i)

#Contagem de 20 até 30 usando laço for
for x in range(20,31):
    print(x,end=" ")

#Contagem 10 até zero usando o laço for
for i in range(10,-1,-1):
    print(i,end=" ")

#Leia 5 números inteiros e mostre uma mensagem quando o número for par
for i in range(5):
    num = int(input("Informe o valor:"))
    if num%2==0:
        print("O valor informado é par")
    else:
        print("O valor informado é ímpar")

#Leia 5 números e some somente os valores ímpares e mostre a quantidade de ímpares
cont = 0
soma = 0
for i in range(5):
    num=int(input("Informe o valor"))
    if num%2!=0:
        soma +=num
        if num%2!=0:
            soma += num
            cont +=1
print(f"A soma dos ímpares é:{soma}")
print(f"A quantidade dos valores ímpares é:{soma}")

#Mostre a média aritmética
print(f"A média de ímpares é {soma/cont:.2f}")