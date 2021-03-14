"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return list(map(lambda x: x ** 2, args))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_numbers, filter_type=PRIME):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 == 1, list_numbers))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, list_numbers))
    elif filter_type == PRIME:
        temp_list_number = list()
        for number in list_numbers:
            if number == 1:
                continue
            elif number > 1:
                it_prime = False
                for denominator in range(1,number):
                    if number % denominator == 0 and denominator != 1 and denominator != number:
                        #list_numbers.remove(number) - Так было бы лучше, но валится тест из за того, что список меняется на лету.
                        it_prime = False
                        break
                    else:
                        it_prime = True
                if it_prime == True:
                    temp_list_number.append(number)
        return temp_list_number

print(filter_numbers([3, 5, 7, 9, 11], PRIME))