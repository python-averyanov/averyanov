def check_brackets(s: str) -> int:
    round = 0
    square = 0
    curly = 0

    for i, char in enumerate(s):
        if char == '(':
            round += 1
        elif char == ')':
            if round == 0:
                return i + 1

            round -= 1
        elif char == '[':
            square += 1
        elif char == ']':
            if square == 0:
                return i + 1

            square -= 1
        elif char == '{':
            curly += 1
        elif char == '}':
            if curly == 0:
                return i + 1
            curly -= 1

    if round > 0 or square > 0 or curly > 0:
        return -1

    return 0  # Все правильно


# Ввод строки
s = input()
print(check_brackets(s))