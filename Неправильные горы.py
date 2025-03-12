def valid_mountain_array(arr):
    n = len(arr)

    if n < 3:
        return False

    i = 0

    # подъем
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # если не было подъема или мы на начале/конце массива
    if i == 0 or i == n - 1:
        return False

    # спуск
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

# Пример чтения массива ввода
import sys
input_data = sys.stdin.read().strip()
height_array = list(map(int, input_data.split()))

# Проверка и вывод результата
result = valid_mountain_array(height_array)
print(result)
