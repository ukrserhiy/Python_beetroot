##The name check.
##Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
##The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
##if your input is “Anton” and the stored name is “anton” it should return True.

lower_name = input('давай имя я переведу в маленькие символы: ')
right_name = str.lower(lower_name)
check_name = input('теперь имя для сравнения: ')
lower_input_name = str.lower(check_name)
if lower_input_name != right_name:
    print('ошибка, не то имя')
else:
    print('это то имя')
