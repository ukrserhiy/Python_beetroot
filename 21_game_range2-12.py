import random

d = list(range(2, 12))
e = random.choice(d)
a = e
x = 22
print('your first result is: ', e)
user_ask = input('yet? Yes or No ')
# первый бросок от пользователя
if e < x and user_ask == 'yes':
    e = random.choice(d)
    print('your result is', e)
    a += e
    print('total is: ', a)
    user_ask = input('yet? Yes or No ') if a < x else print('Your game is done')
    if user_ask == 'yes':
        # второй бросок
        e = random.choice(d)
        print('your result is', e)
        a += e
        print('total is: ', a)
        user_ask = input('yet? ') if a < x else print('Your game is done')
        if a < x and user_ask == 'yes':
            # третий бросок
            e = random.choice(d)
            print('your result is', e)
            a += e
            print('total is: ', a)
            user_ask = input('yet? ') if a < x else print('Your game is done')
            if a < x and user_ask == 'yes':
                # четвертый бросок
                e = random.choice(d)
                print('your result is', e)
                a += e
                print('total is: ', a)
                user_ask = input('yet? ') if a < x else print('Your game is done')
                if a < x and user_ask == 'yes':
                    # пятый бросок
                    e = random.choice(d)
                    print('your result is', e)
                    a += e
                    print('total is: ', a)
                    user_ask = input('yet? ') if a < x else print('Your game is done')
                    if a < x and user_ask == 'yes':
                        # шестой бросок
                        e = random.choice(d)
                        print('your result is', e)
                        a += e
                        print('total is: ', a)
                        user_ask = input('yet? ') if a < x else print('Your game is done')
                        if a < x and user_ask == 'yes':
                            # шестой бросок
                            e = random.choice(d)
                            print('your result is', e)
                            a += e
                            print('total is: ', a)
                            user_ask = input('yet? ') if a < x else print('Your game is done')
if a > x:
    print('You lost')
else:
    print('Let\'s wait for another player')

result_1 = a
print('The final result is: ', a)

e = random.choice(d)
a = e
print('Second player: your first result is: ', e)
user_ask = input('yet? Yes or No ')
# первый бросок от второго пользователя
if e < x and user_ask == 'yes':
    e = random.choice(d)
    print('your result is', e)
    a += e
    print('total is: ', a)
    user_ask = input('yet? Yes or No  ') if a < x else print('Your game is done')
    if user_ask == 'yes':
        # второй бросок
        e = random.choice(d)
        print('your result is', e)
        a += e
        print('total is: ', a)
        user_ask = input('yet? ') if a < x else print('Your game is done')
        if a < x and user_ask == 'yes':
            # третий бросок
            e = random.choice(d)
            print('your result is', e)
            a += e
            print('total is: ', a)
            user_ask = input('yet? ') if a < x else print('Your game is done')
            if a < x and user_ask == 'yes':
                # четвертый бросок
                e = random.choice(d)
                print('your result is', e)
                a += e
                print('total is: ', a)
                user_ask = input('yet? ') if a < x else print('Your game is done')
                if a < x and user_ask == 'yes':
                    # пятый бросок
                    e = random.choice(d)
                    print('your result is', e)
                    a += e
                    print('total is: ', a)
                    user_ask = input('yet? ') if a < x else print('Your game is done')
                    if a < x and user_ask == 'yes':
                        # шестой бросок
                        e = random.choice(d)
                        print('your result is', e)
                        a += e
                        print('total is: ', a)
                        user_ask = input('yet? ') if a < x else print('Your game is done')
                        if a < x and user_ask == 'yes':
                            # шестой бросок
                            e = random.choice(d)
                            print('your result is', e)
                            a += e
                            print('total is: ', a)
                            user_ask = input('yet? ') if a < x else print('Your game is done')

if a > x:
    print('You lost ')
else:
    print('The final result of second player is: ', a)
result_2 = a

print(F'The final result of first player is: {result_1}  and Secont Player is  {result_2}')

if result_1 > result_2 and result_1 < x:
    print('The winner is First Plsyer')
if result_2 > result_1 and result_2 < x:
    print('The winner is Second Plsyer')
if result_2 == result_1 and result_1 < x and result_2 < x:
    print('DRAW ничья')

if result_2 >= x and result_1 < x:
    print('The winner is First Plsyer')
if result_1 >= x and result_2 < x:
    print('The winner is Second Plsyer')
if result_1 >= x and result_2 >= x:
    print('You both are losers')

print('Thank you for game')
