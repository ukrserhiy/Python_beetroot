##The valid phone number program.
##Make a program that checks if a string is on the right format for a phone number.
##The program should check that the string contains only numerical characters and is only 10 characters long.
##Print a suitable message depending on the outcome of the string evaluation.

valid_phone_number = input('number ')
import string
numbers = string.digits
b=1

if len(valid_phone_number) != 10:
    print('wrong number, not 10 symbols')
    b=0
else:
    print('10 sumbols - ok')
for i in valid_phone_number:
    if i not in numbers:
        print(i , ' - is not a number')
        b=0
if b!=0:
    print('all is ok, all are numbers, and all of them 10 digits')
