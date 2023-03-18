"""
У вас есть массив чисел, составьте из
них максимальное число. Например:
[61, 228, 9] -> 961228
"""
from random import randint

def input_int(message):
    input_error: bool = True
    while input_error:
        try:
            number = int(input(message))
        except:
            print("Вы ввели не число!")
        else:
            if number > 0:
                input_error = False
            else:
                print("Вы ввели число меньше 1!")
    return number

num = input_int("Введите количество элементов массива: ")
list = [randint(1, 10000) for item in range(num)]

min_lenght_elem = len(str(list[0]))
max_lenght_elem = len(str(list[0]))
for i in range(len(list)):
    if len(str(list[i])) < min_lenght_elem:
        min_lenght_elem = len(str(list[i]))
    if len(str(list[i])) > max_lenght_elem:
        max_lenght_elem = len(str(list[i]))
multiplier = max_lenght_elem // min_lenght_elem + 1

print(list)

for i in range(len(list) - 1):
    position = i
    for j in range(i+1, len(list)):
        temp_i = int(((str(list[i]) * multiplier))[:max_lenght_elem])
        temp_j = int(((str(list[j]) * multiplier))[:max_lenght_elem])
        temp_position = int(((str(list[position]) * multiplier))[:max_lenght_elem])
        if temp_j > temp_position:
            position = j
    temp = list[i]
    list[i] = list[position]
    list[position] = temp
    print(list)


