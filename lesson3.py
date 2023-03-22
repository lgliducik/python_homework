# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

import time

N = int(input("Введите N:"))
l = []
for _ in range(N):
    l.append(int(input("Введите элемент массива:")))
x = int(input("Введите Х:"))

start = time.perf_counter()
count = 0
for i in l:
    if i == x:
        count += 1
end = time.perf_counter()
f_time = end-start
print(count)

start = time.perf_counter()
print(l.count(x))
end = time.perf_counter()
s_time = end-start
print(f_time/s_time)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите n:"))
mass = []
for _ in range(n):
    mass.append(int(input("Введите элемент массива:")))
X = int(input("Введите Х:"))

min_diff = None
nearest_elem = mass[0]
for elem in mass:
    diff = abs(elem-X)
    if min_diff is None or diff <= min_diff:
        min_diff = diff
        nearest_elem = elem

print(nearest_elem)


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12


english_alphabet = {}
english_alphabet = {k: 1 for k in 'AEIOULNSTR'}
english_alphabet1 = {k: 2 for k in 'DG'}
english_alphabet.update(english_alphabet1)
english_alphabet2 = {k: 3 for k in 'BCMP'}
english_alphabet.update(english_alphabet2)
english_alphabet3 = {k: 4 for k in 'FHVWY'}
english_alphabet.update(english_alphabet3)
english_alphabet4 = {k: 5 for k in 'K'}
english_alphabet.update(english_alphabet4)
english_alphabet4 = {k: 8 for k in 'JX'}
english_alphabet.update(english_alphabet4)
english_alphabet5 = {k: 10 for k in 'QZ'}
english_alphabet.update(english_alphabet5)

russian_alphabet = {}
russian_alphabet = {k: 1 for k in 'АВЕИНОРСТ'}
russian_alphabet1 = {k: 2 for k in 'ДКЛМПУ'}
russian_alphabet.update(russian_alphabet1)
russian_alphabet2 = {k: 3 for k in 'БГЁЬЯ'}
russian_alphabet.update(russian_alphabet2)
russian_alphabet3 = {k: 4 for k in 'ЙЫ'}
russian_alphabet.update(russian_alphabet3)
russian_alphabet4 = {k: 5 for k in 'ЖЗХЦЧ'}
russian_alphabet.update(russian_alphabet4)
russian_alphabet4 = {k: 8 for k in 'ШЭЮ'}
russian_alphabet.update(russian_alphabet4)
russian_alphabet5 = {k: 10 for k in 'ФЩЪ'}
russian_alphabet.update(russian_alphabet5)

word = input("Введите слово:").upper()
price = 0
if word[0] in english_alphabet.keys():
    for symb in word:
        price += english_alphabet[symb]
elif word[0] in russian_alphabet.keys():
    for symb in word:
        price += russian_alphabet[symb]
print(price)
