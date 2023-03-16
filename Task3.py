"""
Задача 14: Требуется вывести все целые степени
двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

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

num = input_int("Введите целое число больше 0: ")

index = 0
temp = 1
while 2**index <= num:
    print(2**index, end = ' ')
    index += 1



