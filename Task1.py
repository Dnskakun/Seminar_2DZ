"""
Задача 10: На столе лежат n монеток. Некоторые из них
лежат вверх решкой, а некоторые – гербом. Определите
минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же
стороной. Выведите минимальное количество монет, которые
нужно перевернуть.
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
            if number > 1:
                input_error = False
            else:
                print("Вы ввели число меньше 2!")
    return number

num = input_int("Введите количество монет больше 1: ")
reshka = randint(0, num)

print(f'Количество монет, лежащее решкой вверх: {reshka}')
print(f'Количество монет, лежащее орлом вверх: {num - reshka}')

if reshka <= num - reshka:
    print(f'Минимальное количество монет, которые надо перевернуть: {reshka}')
else:
    print(f'Минимальное количество монет, которые надо перевернуть: {num - reshka}')




