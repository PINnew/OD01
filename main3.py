# пропишем чем равен факториал 5
# 5! = 1 * 2 * 3 * 4 * 5 = 120

# Сравнение числа с нулем: если число равно 0, то факториал нуля будет равен 1.
# Создание переменной для хранения итогового результата.
# Использование цикла for и range для перебирания списка из чисел до нашего числа включительно, у которого мы ищем факториал.
# Домножение результирующей переменной на текущее число в цикле.
# Возврат факториала числа после цикла.


def factorial(number):
    if number == 0:     # проверяем, равно ли число нулю
        return 1
    result = 1      # создаём переменную для хранения результата
    for i in range(1, number + 1):
        result *= i
    return result
print(factorial(5))