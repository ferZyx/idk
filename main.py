N = 14


def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


array = []
evenCount = 0
for i in range(N):
    element = input(f'Введите {i + 1}-й элемент массива: ')
    isIntKey = isInt(element)
    while not isIntKey:
        element = input(f'Введите {i + 1}-й элемент массива. (Целое число): ')
        isIntKey = isInt(element)
    element = int(element)
    array.append(element)
    if element % 2 == 0:
        evenCount += 1
print(f'Ваш массив.{array}. \nВ нем {evenCount} четных чисел.')
