#Funções com retorno
def soma(v1,v2):
    total = v1+v2
    return total

#Função para calcular a média de três valores
def media_tres(v1,v2,v3):
    return (v1+v2+v3)/3

#Função para mostrar o maior valor a partir de dois números
def mostrar_maior(v1,v2):
    if v1>v2:
        return v1
    else:
        return v2


print(soma(10,20))

#Mostrar o dobro do resultado da função
v1 = soma(100,300)
print(v1*2)

#Calcular a média
print(media_tres(10,8,6))
