# Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
from random import randint
def rand_list(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr


test_list = [randint(1, 99) for i in range(30)]

print(f'Неотсортированный список: {test_list}')
print(f'Отсортированный список: {rand_list(test_list)}')
