#exemplo da função range()
print(list(range(2,20)))
print(list(range(10)))
print(range(10))
print(list(range(10,100,5)))
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