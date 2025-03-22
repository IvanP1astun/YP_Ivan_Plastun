# Считываем количество точек
n = int(input())

# Инициализируем счетчики для каждой четверти
quad1 = 0
quad2 = 0
quad3 = 0
quad4 = 0

# Обрабатываем каждую точку
for _ in range(n):
    x, y = map(int, input().split())

    # Определяем, в какой четверти находится точка
    if x > 0 and y > 0:
        quad1 += 1
    elif x < 0 and y > 0:
        quad2 += 1
    elif x < 0 and y < 0:
        quad3 += 1
    elif x > 0 and y < 0:
        quad4 += 1

# Выводим результаты
print('Первая четверть:', quad1)
print('Вторая четверть:', quad2)
print('Третья четверть:', quad3)
print('Четвертая четверть:', quad4)
