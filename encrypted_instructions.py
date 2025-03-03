# 134374104
def decode_string(code: str)-> str:
    stack = []
    current_num = 0
    current_str = ''

    for char in code:
        if char.isdigit(): # Если символ является цифрой
            current_num = current_num * 10 + int(char) # Собираю число
        elif char == '[': # Если символ открывающая скобка
            stack.append((current_str, current_num)) # Сохраняю текущую строку и число
            current_str = '' # Сбрасываю текущую строку
            current_num = 0 # Сбрасываю текущее число
        elif char == ']': # Если символ закрывающая скобка
            last_str, num = stack.pop() # Берём данные из стека
            current_str = last_str + current_str * num # Формируется новая текущая строка
        else:
            current_str += char # Добавляется символ к текущей строке

    return current_str


if __name__ == '__main__':
    code = input()
    print(decode_string(code))
