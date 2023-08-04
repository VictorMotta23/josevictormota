valor1 = 45
valor2 = 258.45

#operadores aritmeticos
print("Soma:",valor1+valor2)
print("Subtração:",valor1+valor2)
print("multiplicação:",valor1*valor2)
print("Divisão",valor1/valor2)
print(f"Divisão com 2 casas decimais:{valor1/valor2:.2f}")
print(f"valor 2:{valor2:.1f}")
#obter dados do teclado (entrada de dados)
usuario = input("Informe o seu nome:")
print("Seja bem-vindo(a) {usuario}")
#conversão de tipo de dados - Casting
idade = int(input("Informe sua idade:"))
print(f"o nome do usuário é {usuario}e sua idade atual é{idade}")
#mostrar o dobro da idade informada pelo usuario
print(f"O dobro da sua idade é:{idade*2}")
#mostrar tipos de dados das variáveis
print("idade:",type(idade))
print("usuario:",type(usuario))
valor_curso = float(input("Informe o valor pago pelo curso:"))
print(f"O valor informado foi{valor_curso}")
#mostrar uma mensagem com 25% do valor curso
#Parabéns!!! você ganhou <valor> de crédito na próxima compra
vlr_desconto = valor_curso * (25/100)
print(f"Parabéns!!! você ganhou {vlr_desconto} de crédito na próxima compra")
#solicitar quantidade de parcelas do pagamento
parcelas_quantidade =int(input("informe a quantidade de parcelas do pagamento"))
print(f"a quantidade de parcelas informada foi de R$ {valor_curso/parcelas_quantidade:.2f} ")
