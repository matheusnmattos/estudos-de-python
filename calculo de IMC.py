altura=float(input('digite sua altura em metros: '))
peso=float(input('digite o seu peso em kg: '))
imc=peso/altura**2
if imc<18.5:
    print('você esta abaixo do seu peso ideal')
elif imc>=18.5 and imc<=25:
    print('você esta dentro da sua faixa de peso ideal')
elif imc>25 and imc<=30:
    print('você esta com sobrepeso')
elif imc>30 and imc<=40:
    print('você esta com obesidade')
elif imc>40:
    print('você esta com obesidade mórbida')