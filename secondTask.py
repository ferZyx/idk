from random import randint

N = 3
K = 4
array = []
miniArray = []
for i in range(N):
    for j in range(K):
        miniArray.append(randint(0, 20))
    array.append(miniArray)
    miniArray = []
print('Исходная матрица')
for i in range(N):
    print(array[i])

for i in range(N):
    min = array[N - 1][i]
    temp = i
    for j in range(i + 1, K):
        if array[N - 1][j] < min:
            min = array[N - 1][j]
            temp = j
    for k in range(N):
        array[k][temp], array[k][i] = array[k][i], array[k][temp]
print('Отсортированная матрица')
for i in range(N):
    print(array[i])
