#leia o valor de um produto, caso o valor seja menor do que 100 mostre a seguinte mensagem:
#"Você recebeu 5% de desconto", caso contrário
#"Você recebeu 10% de desconto"

valor_prod = float(input("informe o valor do produto:"))

if valor_prod<100:
    print("Você recebeu 5% de desconto")
else:
    print("Você recebeu 10% de desconto")