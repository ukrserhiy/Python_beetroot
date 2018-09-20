##The math quiz program.
##Write a program that asks the answer for a mathematical expression,
##checks whether the user is right or wrong, and then responds with a message accordingly.

import string
import random
digitals = string.digits
math_opers = ('+','-','*','/')
first_element = random.choice(digitals)
second_element = random.choice(digitals)
math_oper=random.choice(math_opers)
result = (first_element, math_oper, second_element, ' равно чему?')
answer = input(result)
if math_oper == '+':
    correct_answer = int(first_element) + int(second_element)
elif math_oper == '-':
    correct_answer = int(first_element) - int(second_element) 
elif math_oper == '*':
    correct_answer = int(first_element) * int(second_element)
elif math_oper == '/':
    correct_answer = int(first_element) / int(second_element) 
else:
    print('ошибка')

if int(answer) != correct_answer:
    print('wrong answer')
else:
    print('correct')

    
