"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент,
а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две
подсказки. 
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
def input_int(message):
    input_error: bool = True
    while input_error:
        try:
            number = int(input(message))
        except:
            print("Вы ввели не число!")
        else:
            input_error = False
    return number

summ = input_int("Введите сумму задуманных чисел: ")
mult = input_int("Введите произведение задуманных чисел: ")
message = "Таких загаданных натуральных чисел не существует!"

# Найдем дискриминант
discrim = summ**2 - 4 * mult
#print(type(summ))
if discrim < 0:
    print(message)
elif discrim == 0:
    x = summ / 2
    if summ % 2 == 0:
        print(f'Петя загадал числа {int(x)} и {int(x)}.')
    else:
        print(message)
else:
    x = (summ - discrim**0.5) / 2
    if (summ - discrim**0.5) % 2 == 0:
        y = summ - x
        print(f'Петя загадал числа {int(x)} и {int(y)}.')
    else:
        print(message)

