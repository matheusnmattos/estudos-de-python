genero=str(input('qual seu gênero?: '))
idade=int(input('qual sua idade?: '))
if genero == 'feminino' :
    print('você não precisa se alistar, apenas o sexo masculino é necessário alistamento obrigatorio')
elif genero == 'masculino' and idade == 18:
    print('você esta na idade para se alistar ao exercito!')
elif genero == 'masculino' and idade > 18:
    print('você ja passou da idade de alistamento')
elif genero == 'masculino' and idade < 18:
    print('você ainda não tem idade para alistamento, apenas com 18 anos você deve se alistar!')
else:
    print('digite as opções validas')