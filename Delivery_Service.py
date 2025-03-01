# ID 134236801
def platforms(data: list[int], limit: int) -> int:
    '''
    Вычисляем минимальное количество необходимых платформ
    для транспортировки роботов, вес которых будет передаваться в data,
    а ограничение по весу на одну платформу в limit.
    '''
    platforms, left_pointer, right_pointer = 0, 0, len(data) - 1

    while left_pointer < right_pointer:
        result = data[left_pointer] + data[right_pointer]
        platforms += 1
        right_pointer -= 1

        if result <= limit:
            left_pointer += 1

    if left_pointer == right_pointer:
        platforms += 1
    return platforms


if __name__ == '__main__':
    data = sorted([int(i) for i in input().split()])
    limit = int(input())
    print(platforms(data, limit))