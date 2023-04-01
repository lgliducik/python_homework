# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

a1 = int(input("Введите a1:"))
d = int(input("Введите d:"))
count_elem = int(input("Введите count_elem:"))


def arith_pr(first, diff, count):
    rez = []
    for i in range(1,count):
        rez.append(first + (i - 1) * diff)
    return rez


print(arith_pr(a1, d, count_elem))


input_min = int(input("Введите input_min:"))
input_max = int(input("Введите input_max:"))
n = int(input("Введите n:"))
mass = []
for _ in range(n):
    mass.append(int(input("Введите элемент массива:")))


def filter_mass(i_min, i_max, input_mass):
    rez_index = []
    for i in range(len(input_mass)):
        if input_mass[i] > i_min and input_mass[i]< i_max:
            rez_index.append(i)
    return rez_index


print(filter_mass(input_min, input_max, mass))
