values = ['6','7','8','9','10','B','D','K','T',]

kinds = ['\u2663','\u2665','\u2666','\u2660',]

CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"
cards = []

# собираем колоду
for value in values:
    for kind in kinds:
        card=value+kind
        #print(card, sep =' ')
        cards.append(card)
print(cards)

import random
print('Let\'s play. ' )
#d = list(range(2,12))
d = cards
e = random.choice(cards)
a = 0
x = 22
print('Your first result is: ',e)
dlt=cards.index(e)
del cards[dlt]
# рисуем карту
def card_picture(e):
    lines = [[] for i in range(9)]
    lines[0].append('┌─────────┐')
    lines[1].append('│'+e+'       │')
    lines[2].append('│         │')
    lines[3].append('│         │')
    lines[4].append('│         │')
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│       '+e+'│')
    lines[8].append('└─────────┘')
    print (lines[0], lines[1], lines[2],lines[3], lines[4],lines[5],lines[6],lines[7],lines[8], sep ="\n")
    return lines
card_picture(e)
# даем численное значение карте
def card_value(e):
    if e == '6♣' or e == '6♥' or e == '6♦' or e == '6♠':
        e=6
    elif e == '7♣' or e == '7♥' or e == '7♦' or e== '7♠':
        e=7
    elif e == '8♣' or  e =='8♥' or e =='8♦' or e =='8♠':
        e=8    
    elif e == '9♣' or e =='9♥' or e =='9♦' or e =='9♠':
        e=9
    elif e== '10♣' or e == '10♥' or e =='10♦' or e == '10♠':
        e=10
    elif e == 'B♣'or e == 'B♥' or e =='B♦' or e ==  'B♠':
        e=2
    elif e == 'D♣' or e == 'D♥' or e =='D♦' or e == 'D♠':
        e=3
    elif e == 'K♣' or e == 'K♥' or e == 'K♦' or e == 'K♠':
        e=4
    elif e == 'T♣' or e =='T♥' or e =='T♦' or e == 'T♠':
        e=11
    return e

user_ask = input('yet? Yes or No ')

# первый бросок от пользователя
e = card_value(e)
a+=e
if int(e) < int(x) and user_ask =='yes' or user_ask =='y' or user_ask == 'Yes' or user_ask == 'Y':
    e = random.choice(d)    
    print('your result is', e)
    dlt=cards.index(e)
    del cards[dlt]
    card_picture(e)
    e = card_value(e)
    a+=e
    print('total is: ', a)
    user_ask = input('yet? Yes or No ') if a < x else print ('Your game is done')
    if user_ask == 'yes':
        # второй бросок
        e = random.choice(d)
        print('your result is', e)
        dlt=cards.index(e)
        del cards[dlt]
        card_picture(e)
        e = card_value(e)
        a+=e
        print('total is: ', a)
        user_ask = input('yet? ') if a < x else print ('Your game is done')
        if a < x and user_ask == 'yes':
             # третий бросок
             e = random.choice(d)
             print('your result is', e)
             dlt=cards.index(e)
             del cards[dlt]
             card_picture(e)
             e = card_value(e)
             a+=e
             print('total is: ', a)
             user_ask = input('yet? ') if a < x else print ('Your game is done')
             if a < x and user_ask == 'yes':
                 # четвертый бросок
                 e = random.choice(d)
                 print('your result is', e)
                 dlt=cards.index(e)
                 del cards[dlt]
                 card_picture(e)
                 e = card_value(e)
                 a+=e
                 print('total is: ', a)
                 user_ask = input('yet? ') if a < x else print ('Your game is done')
                 if a < x and user_ask == 'yes':
                    # пятый бросок
                    e = random.choice(d)
                    print('your result is', e)
                    dlt=cards.index(e)
                    del cards[dlt]
                    card_picture(e)
                    e = card_value(e)
                    a+=e
                    print('total is: ', a)
                    user_ask = input('yet? ') if a < x else print ('Your game is done')
                    if a < x and user_ask == 'yes':
                       # шестой бросок
                       e = random.choice(d)
                       print('your result is', e)
                       dlt=cards.index(e)
                       del cards[dlt]
                       card_picture(e)
                       e = card_value(e)
                       a+=e
                       print('total is: ', a)
                       user_ask = input('yet? ') if a < x else print ('Your game is done')
                       if a < x and user_ask == 'yes':
                           # шестой бросок
                           e = random.choice(d)
                           print('your result is', e)
                           dlt=cards.index(e)
                           del cards[dlt]
                           card_picture(e)
                           e = card_value(e)
                           a+=e
                           print('total is: ', a)
                           user_ask = input('yet? ') if a < x else print ('Your game is done')

if a > x:
    print('You lost')
else:
    print('Let\'s wait for another player')
  
result_1=a   
print('The final result is: ', a)

a=0
e=0
e = random.choice(d)
dlt=cards.index(e)
del cards[dlt]
card_picture(e)
e = card_value(e)
a = e
print('Second player: your first result is: ',e)
user_ask = input('yet? Yes or No ')
# первый бросок от второго пользователя
if e < x and user_ask =='yes':
    e = random.choice(d)
    print('your result is', e)
    dlt=cards.index(e)
    del cards[dlt]
    card_picture(e)
    e = card_value(e)
    a+=e
    print('total is: ', a)
    user_ask = input('yet? Yes or No  ') if a < x else print ('Your game is done')
    if user_ask == 'yes':
        # второй бросок
        e = random.choice(d)
        print('your result is', e)
        dlt=cards.index(e)
        del cards[dlt]
        card_picture(e)
        e = card_value(e)
        a+=e
        print('total is: ', a)
        user_ask = input('yet? ') if a < x else print ('Your game is done')
        if a < x and user_ask == 'yes':
             # третий бросок
             e = random.choice(d)
             print('your result is', e)
             dlt=cards.index(e)
             del cards[dlt]
             card_picture(e)
             e = card_value(e)
             a+=e
             print('total is: ', a)
             user_ask = input('yet? ') if a < x else print ('Your game is done')
             if a < x and user_ask == 'yes':
                 # четвертый бросок
                 e = random.choice(d)
                 print('your result is', e)
                 dlt=cards.index(e)
                 del cards[dlt]
                 card_picture(e)
                 e = card_value(e)
                 a+=e
                 print('total is: ', a)
                 user_ask = input('yet? ') if a < x else print ('Your game is done')
                 if a < x and user_ask == 'yes':
                    # пятый бросок
                    e = random.choice(d)
                    print('your result is', e)
                    dlt=cards.index(e)
                    del cards[dlt]
                    card_picture(e)
                    e = card_value(e)
                    a+=e
                    print('total is: ', a)
                    user_ask = input('yet? ') if a < x else print ('Your game is done')
                    if a < x and user_ask == 'yes':
                       # шестой бросок
                       e = random.choice(d)
                       print('your result is', e)
                       dlt=cards.index(e)
                       del cards[dlt]
                       card_picture(e)
                       e = card_value(e)
                       a+=e
                       print('total is: ', a)
                       user_ask = input('yet? ') if a < x else print ('Your game is done')
                       if a < x and user_ask == 'yes':
                           # шестой бросок
                           e = random.choice(d)
                           print('your result is', e)
                           dlt=cards.index(e)
                           del cards[dlt]
                           card_picture(e)
                           e = card_value(e)
                           a+=e
                           print('total is: ', a)
                           user_ask = input('yet? ') if a < x else print ('Your game is done')

if a > x:
    print('You lost ')
else:      
   print('The final result of second player is: ', a)
result_2=a

print(F'The final result of first player is: {result_1}  and Second Player is  {result_2}')

if result_1>result_2 and result_1 < x:
    print('The winner is First Plsyer')
if result_2>result_1 and result_2 < x:
    print('The winner is Second Plsyer')
if result_2==result_1 and result_1 < x and result_2 < x:
    print('DRAW ничья')
    
if result_2>=x and result_1 < x:
    print('The winner is First Plsyer')
if result_1>=x and result_2 < x:
    print('The winner is Second Plsyer')
if result_1 >= x and result_2 >= x:
    print('You both are losers')

    
print('Thank you for game')
