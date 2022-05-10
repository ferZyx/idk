N = 10
array = []
for i in range(N):
    value = input(f'Введите символ для {i + 1}-ого элемента массива: ')
    array.append(value)
print(f'Исходный массив: {array}')
for i in range(N):
    if array[i].isdigit():
        array[i] = '*'
print(f'Итоговый массив: {array}')
