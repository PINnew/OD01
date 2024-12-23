# 1. Удаляем пробелы и приводим к нижнему регистру
# 2. Создаем обратную строку
# 3. Сравниваем оригинальную и обратную строки
# 4. Возвращаем результат



def is_palindrome(s):
    # 1. Удаляем пробелы и приводим к нижнему регистру
    cleaned_string = ''.join(s.split()).lower()

    # 2. Создаем обратную строку
    reversed_string = cleaned_string[::-1]

    # 3. Сравниваем оригинальную и обратную строки
    # 4. Возвращаем результат
    return cleaned_string == reversed_string


# Примеры использования функции
if __name__ == "__main__":
    test_strings = ["A man a plan a canal Panama", "Hello", "Racecar", "Was it a car or a cat I saw?"]

    for string in test_strings:
        result = is_palindrome(string)
        print(f'"{string}" is a palindrome: {result}')
