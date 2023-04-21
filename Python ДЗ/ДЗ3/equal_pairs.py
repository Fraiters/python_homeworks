import sys

try:
    length_list = int(input("Введите количество элементов в списке: "))
    _list = [int(length_list) for length_list in input("Введите элементы "
                                                       "списка через пробел: ").split()]
except ValueError:
    sys.exit(1)
count = 0
for i in range(len(_list) - 1):
    for j in range(len(_list) - i - 1):
        if _list[i] == _list[j + i + 1]:
            count += 1
print(count)
