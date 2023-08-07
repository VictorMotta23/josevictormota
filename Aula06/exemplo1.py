#Aula de listas"

lista = [2,8,10,4,55,'coxinha',34,'hellmanns',33]
print(type(lista))
print("Primeiro item da lista:",lista[0])
print("Último item da lista:",[8])
print("Último item da lista",lista[-1])
print("Penúltimo item da lista:",lista[-2])
print("Quantidade de itens da lista:",len(lista))
# print("Lista ordenada:",sorted(lista))
pc = ["Mouse","Monitor","HD","Memória RAM","Câmera"]
#Mostrar lista em ordem conforme os itens
print(sorted(pc))
lista2 = [6,9,4,12,50,0,2]
print(sorted(lista2))
#Mostrar intervalos da lista
print(lista2)
print(lista2[2:5])
print(lista2[3:])
print(lista2[:4])
lista2.append(1000)
print(lista2)
#Inserir item em posição determinada na lista
lista2.insert(2,5000)
print(lista2)
#Unir duas listas
lista2.extend(lista)
print(lista2)
#Remover úlitimo item da lista ou o índice informado
lista2.pop()
print(lista2)
#Remover item específico da lista
lista2.remove('coxinha')
print(lista2)