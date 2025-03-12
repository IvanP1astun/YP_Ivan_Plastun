def count_jewels(J, S):
    # Превращаем J в множество для быстрого поиска
    jewels = set(J)
    # Считаем количество драгоценностей в S
    count = sum(1 for stone in S if stone in jewels)
    return count

# Чтение входных данных
with open('input.txt', 'r') as f:
    J = f.readline().strip()
    S = f.readline().strip()

# Получение результата
result = count_jewels(J, S)

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(str(result) + '\n')
