primeiro=int(input('digite o primeiro numero: '))
segundo=int(input('digite o segundo numero: '))
terceiro=int(input('digite o terceiro numero: '))
if primeiro> segundo and primeiro> terceiro:
    print(' o maior numero é o {} que foi o primeiro que você digitou'.format(primeiro))
elif segundo>primeiro and segundo> terceiro:
        print('o maior numero é o {} que foi o segundo que você digitou'.format(segundo))
else:
            print('o maior numero é o {} que foi o terceiro que você digitou'.format(terceiro))

if primeiro<segundo and primeiro<terceiro:
                print('o menor numero é o {} que foi o primeiro que você digitou'. format(primeiro))
elif segundo < primeiro and segundo<terceiro:
                    print('o menor numero é o {} que foi o segundo numero que você digitou'.format(segundo))
else:
                        print('o menor numero é o {} que foi o terceiro numero que você digitou'.format(terceiro))