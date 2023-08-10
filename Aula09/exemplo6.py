#Abertura de um arquivo chamado dados2.txt
#Ler o nome de uma pessoa

try:
    txt = open("aula09/dados2.txt","a+")
    for i in range(1,11):
        nome = input("Informe o nome do cidadão:")
        txt.write(f"{i} - Nome:{nome}/n")
except:
    print("Não foi possível localizar o arquivo!")
else:
    txt.seek(0)
    print(txt.read())
    txt.close()