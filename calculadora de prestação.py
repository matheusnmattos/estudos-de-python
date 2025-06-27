casa=float(input('qual valor em reais da casa que você deseja comprar R$: '))
salario=float(input('qual valor do seu salario em reais R$: '))
tempo=int(input('em quantos anos você deseja pagar a casa?:'))
tempo = tempo*12
prestacao = casa/tempo
if prestacao <= salario*0.30:
    print('parabéns, seu emprestimo foi aprovado, as parcelas mensais ficarão de R${:.2f}'.format(prestacao))
else:
    print('infelizmente o seu emprestimo não foi aprovado, pois a prestação mensal supera em 30% o seu salário!')
