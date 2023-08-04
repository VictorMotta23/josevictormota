#leia a iaade do usuário e informe se ele é maior ou menor de idade
#Verificar números negativos antes da idade
idade = int(input("informe sua idade:"))

if idade<0:
    print("Idade inválida!!!")
    print("Verifique o valor informado.")
 else:     
if idade>=18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")