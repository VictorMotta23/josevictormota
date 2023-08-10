#Trabalhar com estrutura de dados dicionário(dict)

dados = {}
print(type(dados))
alunos = {111:"Karla da Silva",222:"Hélio Mota",333:"Júlia Mota",444:"Sheila Lopes"}

#Mostrar primeiro item do dicionário
print(alunos[111])

#Mostrar somente as chaves do dicionário
print(alunos.keys())

#Mostrar somente os valores armazenados no dicionário
print(alunos.values())

#Mostrar todos os itens do dicionário
print(alunos.items())

#Atualizar dicionário
alunos.update({555:"José Victor"})
print(alunos)
alunos[666] = "Teste"
print(alunos)
alunos[111] = "Carlos Manoel"
print(alunos)

#Excluir um item do dicionário
alunos.pop(666)
print(alunos)

#Mostrar somente os valores do dicionário
for i in alunos.values():
    print(i)

#Mostrar somente as chaves do dicionário
for i in alunos.keys():
    print(i)
    
#Mostrar todos os itens de um dicionário
for i in alunos.items():
    print(i)

for i,j in alunos.items():
    print(i,j,sep=" 🍕 ")


dados = {
    'lista_a':[1,2,2,5,8],
    'Lista_b':[10,20,30,40],
    'Lista_c':[100,200,300,400]
}
print(dados)
print(type(dados))

#Mostrar último item da lista b
print(dados["lista_b"][-1])