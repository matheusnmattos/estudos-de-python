num1=int(input('digite o valor do primeiro número para comparação: '))
num2=int(input('digite o valor do segundo número para comparação: '))
if num1>num2:
    print('o primeiro número que você digitou que é {} é maior que o segundo número que é {}'.format(num1,num2))
elif num2>num1:
    print('o segundo número que você digitou {} é maior que o primeiro número que você digitou que é {}'.format(num2,num1))
else:
    print('não existe valor maior, os dois são iguais')
