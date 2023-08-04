#Estrutura de repetição while(continuação)
#Leia 5 números e mostre a soma de todos os valores informados

cont = 1
soma = 0 #acumulador

# while cont<=5:
#     num = float(input("informe um valor"))
#     soma += num
#     cont =+1
    
    # print("Resultado da soma é:",soma)
    #Calcular a soma dos valores do intervalo(fechado) das variáveis a e b (280)
a = 10
b = 25
ac = 0
while a<=b:
    print(a,end=" ")
    ac += a
    a += 1

print("\nO resultado é:", ac)
#Leia 2 valores e mostre a soma do intervalo entre eles
v1 = int(input("Informe o valor inicial:"))
v2 = int(input("Informe o valor final:"))
soma = 0
if v1<v2:
    while v1<=v2:
        soma += v1
        v1 += 1
    print("O resultado é:",soma)
elif v2<v1:
    while v2<=v1:
        soma += v2
        v2 +=1
    print("O resultado é:",soma)
else:
    print("Os valores são iguais =(")

#Somar 5 valores positivos informados pelo usuário
soma = 0
cont = 1

while cont<=5:
    valor = float(input("Informe um valor positivo!"))
    if valor<0:
        continue
    soma += valor
    cont+=1
print (f"O resultado da soma é {soma}")

#Somar 5 valores negativos informados pelo usuário
ac = 0
cont = 1       
while cont<=5:
    valor = float(input("Informe um valor negativo:"))
    if valor>=0:
        print("Eu não creio...")
        break
    ac += valor
    cont += 1
print(f"O resultado da soma é {ac}")
#Leia 3 notas e mostre a média, caso seja digitado um valor negativo ou acima de 10 será solicitado um novo valor
soma = 0
cont = 1
while cont<=3:
    nota = float(input("Informe a nota:"))
    if nota<0 or nota>10:
        continue
    soma += nota
    cont += 1
print(f"A soma das notas informadas é {soma}")
print(f"A média dos valores informados é {soma/3:.2f}")
