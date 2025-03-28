# 134435629
import string
from typing import List, Tuple


OPEN_BRACKET = '['
CLOSE_BRACKET = ']'
ZERO = 0
THE_CONSTANT = 10
digits_set = set(string.digits)

def decode_string(code: str)-> str:
    stack: List[Tuple[str, int]] = []
    current_num = 0
    current_str = ''

    for char in code:
        if char in digits_set: # Если символ является цифрой
            current_num = current_num * THE_CONSTANT + int(char) # Собираю число
        elif char == OPEN_BRACKET: # Если символ открывающая скобка
            stack.append((current_str, current_num)) # Сохраняю текущую строку и число
            current_str = '' # Сбрасываю текущую строку
            current_num = ZERO # Сбрасываю текущее число
        elif char == CLOSE_BRACKET: # Если символ закрывающая скобка
            last_str, num = stack.pop() # Берём данные из стека
            current_str = last_str + current_str * num # Формируется новая текущая строка
        else:
            current_str += char # Добавляется символ к текущей строке

    return current_str


if __name__ == '__main__':
    code = input()
    print(decode_string(code))
