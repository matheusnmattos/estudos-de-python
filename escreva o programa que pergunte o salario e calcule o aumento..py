salario=float(input('digite o valor do seu salario em reais R$ '))
if salario>1250.00:
    aumento=salario*0.10
    salario_novo= salario+aumento
else:
    aumento=salario*0.15
    salario_novo= salario+aumento
print('parabéns você terá um aumento! Seu salário passará ser de R${}'.format(salario_novo))