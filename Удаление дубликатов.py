# Чтение входных данных
n = int(input())
array = list(map(int, input().split()))

# Список для уникальных элементов и счетчик дубликатов
unique_elements = []
duplicates_count = 0

# Разделяем уникальные элементы и считаем дубликаты
for num in array:
    if num not in unique_elements:
        unique_elements.append(num)
    else:
        duplicates_count += 1

# Формируем результирующий массив
result = unique_elements + ['_'] * duplicates_count

# Вывод результата
print(" ".join(map(str, result)))
