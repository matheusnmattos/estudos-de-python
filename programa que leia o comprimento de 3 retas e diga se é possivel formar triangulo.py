lado1=float(input('digite o comprimento da primeira reta: '))
lado2=float(input('digite o comprimento da segunda reta: '))
lado3=float(input('digite o comprimento da terceira reta: '))
if lado1+lado2>lado3 and lado2+lado3>lado1 and lado1+lado3>lado2:
    print('sim, essas retas podem formar um triângulo!')
else:
    print('não, essas retas não podem formar um triângulo!')

if lado1**2+lado2**2==lado3**2 or lado2**2+lado3**2==lado1**2 or lado1**2+lado3**2==lado2**2:
    print('nesse caso ele também é um triangulo retangulo')
else:
    print('mas não é um triangulo retangulo!')
