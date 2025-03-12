def longest_unique_substring(s):
    char_index = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        # Если символ уже встречался, сдвигаем окно
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        # Обновляем индекс текущего символа
        char_index[char] = i
        # Вычисляем максимальную длину
        max_length = max(max_length, i - start + 1)

    return max_length

if __name__ == '__main__':
    input_string = input()  # Ввод строки
    result = longest_unique_substring(input_string)
    print(result)  # Вывод длины самой длинной подстроки с уникальными символами
