"""
Hangman
1. есть файл со списком слов
2. случайным образом взять слово (печатаем в верхнем регистре)
3. # done показать его длину
4. пользователь вводит в консоль букву (в любом регистре)
5. показываем если угадал - что ок и ставим букву на нужную место
6. если не угадал - показываем что ошибка (рисуем часть виселицы)
7. добавить названную букву в список (set) названных букв
8. когда угадал слово - выиграл
9. когда не угадал три раза - проиграл
10. если не угадал но эта буква уже была названа - ошибку не добавлять
11. # done сделать вариант - досрочного выхода - ввод символа "-",

"""
def card_picture_0():
    lines = [[] for i in range(9)]
    lines[0].append('┌─────────┐')
    lines[1].append('│   |     │')
    lines[2].append('│   |     │')
    lines[3].append('│   0     │')
    lines[4].append('│  /|\    │')
    lines[5].append('│  /\     │')
    lines[6].append('│         │')
    lines[7].append('│         │')
    lines[8].append('└─────────┘')
    print (lines[0], lines[1], lines[2],lines[3], lines[4],lines[5],lines[6],lines[7],lines[8], sep ="\n")
    return lines

def card_picture_1():
    lines = [[] for i in range(9)]
    lines[0].append('┌─────────┐')
    lines[1].append('│   |     │')
    lines[2].append('│   |     │')
    lines[3].append('│   0     │')
    lines[4].append('│  /|\    │')
    lines[5].append('│  /      │')
    lines[6].append('│         │')
    lines[7].append('│         │')
    lines[8].append('└─────────┘')
    print (lines[0], lines[1], lines[2],lines[3], lines[4],lines[5],lines[6],lines[7],lines[8], sep ="\n")
    return lines

def card_picture_2():
    lines = [[] for i in range(9)]
    lines[0].append('┌─────────┐')
    lines[1].append('│   |     │')
    lines[2].append('│   |     │')
    lines[3].append('│   0     │')
    lines[4].append('│  /|\    │')
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│         │')
    lines[8].append('└─────────┘')
    print (lines[0], lines[1], lines[2],lines[3], lines[4],lines[5],lines[6],lines[7],lines[8], sep ="\n")
    return lines

def card_picture_3():
    lines = [[] for i in range(9)]
    lines[0].append('┌─────────┐')
    lines[1].append('│   |     │')
    lines[2].append('│   |     │')
    lines[3].append('│   0     │')
    lines[4].append('│  /|     │')
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│         │')
    lines[8].append('└─────────┘')
    print (lines[0], lines[1], lines[2],lines[3], lines[4],lines[5],lines[6],lines[7],lines[8], sep ="\n")
    return lines

def card_picture_4():
    lines = [[] for i in range(9)]
    lines[0].append('┌─────────┐')
    lines[1].append('│   |     │')
    lines[2].append('│   |     │')
    lines[3].append('│   0     │')
    lines[4].append('│  /      │')
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│         │')
    lines[8].append('└─────────┘')
    print (lines[0], lines[1], lines[2],lines[3], lines[4],lines[5],lines[6],lines[7],lines[8], sep ="\n")
    return lines



def card_picture_5():
    lines = [[] for i in range(9)]
    lines[0].append('┌─────────┐')
    lines[1].append('│   |     │')
    lines[2].append('│   |     │')
    lines[3].append('│   0     │')
    lines[4].append('│         │')
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│         │')
    lines[8].append('└─────────┘')
    print (lines[0], lines[1], lines[2],lines[3], lines[4],lines[5],lines[6],lines[7],lines[8], sep ="\n")
    return lines


def card_picture_6():
    lines = [[] for i in range(9)]
    lines[0].append('┌─────────┐')
    lines[1].append('│   |     │')
    lines[2].append('│   |     │')
    lines[3].append('│         │')
    lines[4].append('│         │')
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│         │')
    lines[8].append('└─────────┘')
    print (lines[0], lines[1], lines[2],lines[3], lines[4],lines[5],lines[6],lines[7],lines[8], sep ="\n")
    return lines

#создать файл со списком слов и взять первое
#F = open('workfile.txt','r')
#our_word= F.readlines(1)

#выбираем слова из файла случайным образом
# наше слово
our_word = list('silver')
user_wrong_list = []
user_right_list = []
len_our_word = len(our_word)
error=0
import string
#пользователь в терминал вводит буквы
print('Кол-во букв в слове: ',  len_our_word)
while len(user_right_list) < len(our_word):
   user_symbol = input('введи букву: ')
   if user_symbol not in string.ascii_letters:
       print('ты ввел не тот символ')
   if user_symbol == '-':
       break
   else:
#если буква входит в слово, то поздравляем пользователя
       if user_symbol in  our_word and user_symbol in string.ascii_letters:
           place= (our_word.index(user_symbol)+1)
           print('угадал, эта буква в слове на ', place, ' месте')
           if user_symbol not in user_right_list:
               user_right_list.append(user_symbol)
           else:
               print('Альцгеймер, ты уже называл эту букву, и да, она есть в слове на ', place, ' месте')
           print('ты уже неправильно называл такие буквы как ', user_wrong_list, ' и угадал такие буквы как: ', user_right_list)    
#если буква не входит в слово, то элемент виселицы рисуется.
       elif user_symbol not in  our_word and user_symbol in string.ascii_letters:
             
            print('ошибся')
            if user_symbol not in user_wrong_list and user_symbol not in user_right_list:
                user_wrong_list.append(user_symbol)
                error+=1
            else:
                print('Альцгеймер, ты уже называл эту букву, и нет, ее нет в слове')
            print('ты уже неправильно называл такие буквы как ', user_wrong_list, ' и угадал такие буквы как: ', user_right_list)
       else:
           print('пробуй еще')

       if error==1:
           card_picture_6()
       elif error==2:
           card_picture_5()
       elif error==3:
           card_picture_4()
       elif error==4:
           card_picture_3()
       elif error==5:
           card_picture_2()
       elif error==6:
           card_picture_1()
       elif error==7:
           card_picture_0()
           break
        
print('Игра окончена')
if len(user_right_list) == len(our_word):
    print('ты выиграл, слово было: ', our_word)
else:
    print('проиграл')            
        




