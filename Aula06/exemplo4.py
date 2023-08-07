#Tupla

cidades = ('Manaus','Tefé','Parintins','Manacupuru')
print(type(cidades))
#Mostrar o último item da tupla
print(cidades[-1])
#Mostrar o primeiro item da tupla
print(cidades[0])
#Mostrar itens ordenados
print(sorted(cidades))
print(cidades.count('Manaus'))
#Leia 3 números positivos e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor informado e o menor valor informado.
cont = 1 
lista1 = []
while cont<=3:
    num=float(input("Informe o valor:"))
    lista1.append(num)
    cont +=1
print("Lista ordenada:",sorted(lista1))
print("Maior valor:",max(lista1))
print("Menor valor:",min(lista1))    
