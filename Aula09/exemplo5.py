try:
    txt = open("aula09/dados.txt","a+")
    print("Arquivo encontrado!")
    txt.seek(0)
    print(txt.read())
except:
    print("Problemas ao executar o arquivo...")
