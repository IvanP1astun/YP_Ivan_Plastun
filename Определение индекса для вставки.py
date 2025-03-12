def find_insert_index(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            # Найден элемент
            while mid > 0 and array[mid - 1] == target:
                mid -= 1
            return mid  # Возвращаем индекс первого вхождения

    return left  # Индекс, под которым могло бы находиться значение

# Чтение входных данных
input_array = list(map(int, input().split()))
target_value = int(input().strip())

# Поиск индекса
index = find_insert_index(input_array, target_value)

# Вывод результата
print(index)
