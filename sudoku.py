# строки судоку
row_1 = [0,0,0,3,4,0,0,7,6]
row_2 = [0,0,0,0,7,1,4,3,0]
row_3 = [0,7,3,0,0,0,0,8,1]
row_4 = [2,0,9,7,6,0,0,0,0]
row_5 = [7,3,4,0,9,0,0,0,0]
row_6 = [8,0,0,1,3,2,0,0,9]
row_7 = [9,0,8,0,0,7,1,0,0]
row_8 = [3,4,2,9,0,0,0,6,0]
row_9 = [1,0,0,6,8,0,0,0,0]

print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)
print(row_6)
print(row_7)
print(row_8)
print(row_9)

all_of_rows = row_1+row_2+row_3+row_4+row_5+row_6+row_7+row_8+row_9

# столбцы судоку 
column_1 = [row_1[0], row_2[0], row_3[0],row_4[0],row_5[0],row_6[0],row_7[0],row_8[0],row_9[0]]
column_2 = [row_1[1], row_2[1], row_3[1],row_4[1],row_5[1],row_6[1],row_7[1],row_8[1],row_9[1]]
column_3 = [row_1[2], row_2[2], row_3[2],row_4[2],row_5[2],row_6[2],row_7[2],row_8[2],row_9[2]]

column_4 = [row_1[3], row_2[3], row_3[3],row_4[3],row_5[3],row_6[3],row_7[3],row_8[3],row_9[3]]
column_5 = [row_1[4], row_2[4], row_3[4],row_4[4],row_5[4],row_6[4],row_7[4],row_8[4],row_9[4]]
column_6 = [row_1[5], row_2[5], row_3[5],row_4[5],row_5[5],row_6[5],row_7[5],row_8[5],row_9[5]]

column_7 = [row_1[6], row_2[6], row_3[6],row_4[6],row_5[6],row_6[6],row_7[6],row_8[6],row_9[6]]
column_8 = [row_1[7], row_2[7], row_3[7],row_4[7],row_5[7],row_6[7],row_7[7],row_8[7],row_9[7]]
column_9 = [row_1[8], row_2[8], row_3[8],row_4[8],row_5[8],row_6[8],row_7[8],row_8[8],row_9[8]]


# квадраты судоку
square_1 = [row_1[0], row_2[0], row_3[0], row_1[1], row_2[1], row_3[1], row_1[2], row_2[2], row_3[2]]
square_2 = [row_1[3], row_2[3], row_3[3], row_1[4], row_2[4], row_3[4], row_1[5], row_2[5], row_3[5]]
square_3 = [row_1[6], row_2[6], row_3[6], row_1[7], row_2[7], row_3[7], row_1[8], row_2[8], row_3[8]]

square_4 = [row_4[0], row_5[0], row_6[0], row_4[1], row_5[1], row_6[1], row_4[2], row_5[2], row_6[2]]
square_5 = [row_4[3], row_5[3], row_6[3], row_4[4], row_5[4], row_6[4], row_4[5], row_5[5], row_6[5]]
square_6 = [row_4[6], row_5[6], row_6[6], row_4[7], row_5[7], row_6[7], row_4[8], row_5[8], row_6[8]]

square_7 = [row_7[0], row_8[0], row_9[0], row_7[1], row_8[1], row_9[1], row_7[2], row_8[2], row_9[2]]
square_8 = [row_7[3], row_8[3], row_9[3], row_7[4], row_8[4], row_9[4], row_7[5], row_8[5], row_9[5]]
square_9 = [row_7[6], row_8[6], row_9[6], row_7[7], row_8[7], row_9[7], row_7[8], row_8[8], row_9[8]]



set_row_1 = set(row_1)
set_row_2 = set(row_2)
set_row_3 = set(row_3)
set_row_4 = set(row_4)
set_row_5 = set(row_5)
set_row_6 = set(row_6)
set_row_7 = set(row_7)
set_row_8 = set(row_8)
set_row_9 = set(row_9)


# с самого начала есть эти цифры
exist_from_start_ = list(set().union(row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9))
exist_from_start =set(exist_from_start_)
print('с самого начала есть эти цифры  ', exist_from_start)

# список всех возможных цифр
all_numbers_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
all_numbers = set(all_numbers_ ) 


# пока вообще нет этих цифр
absence_numbers = all_numbers.symmetric_difference(exist_from_start)
print('пока вообще нет этих цифр  ', absence_numbers)


total_quantity_cells = len(row_1) + len(row_2) + len(row_3) +len(row_4)+ len(row_5)+ len(row_6)+ len(row_7)+ len(row_8)+ len(row_9)
print('всего клеток с цифрами ', total_quantity_cells)
total_quantity_empty = row_1.count(0) + row_2.count(0) + row_3.count(0)+row_4.count(0)+ row_5.count(0)+ row_6.count(0)+ row_7.count(0) +row_8.count(0) + row_9.count(0)
print('всего пустых клеток ', total_quantity_empty)


possibility = (100* total_quantity_empty) / total_quantity_cells


print('Процент неизвестных значений ', int(possibility), '%')


if row_1[0] == 0:
    vse_in_1 = list(set().union(row_1, column_1, square_1))
    lack_first_ = all_numbers.symmetric_difference(vse_in_1)
    lack_first = list(lack_first_)
    if len(lack_first) == 1:
        print('новое значение: ', lack_first, 'на место', row_1[0]   )
        row_1[0] = lack_first
        print(row_1)
        
