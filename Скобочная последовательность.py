def is_correct_bracket_seq(sequence):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in bracket_pairs.values():  # Если это открывающая скобка
            stack.append(char)
        elif char in bracket_pairs.keys():  # Если это закрывающая скобка
            if not stack:
                return False  # Нет соответствующей открывающей скобки
            if stack.pop() != bracket_pairs[char]:
                return False  # Неправильная пара скобок

    return len(stack) == 0  # Если стек пуст, последовательность правильная

# Пример использования
input_sequence = input().strip()  # Чтение входной строки
result = is_correct_bracket_seq(input_sequence)
print(result)  # Вывод результата
