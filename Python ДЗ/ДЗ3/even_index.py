import sys

try:
    length_list = int(input("Введите количество элементов в списке: "))
    _list = [int(length_list) for length_list in input("Введите элементы "
                                                       "списка через пробел: ").split()]
except ValueError:
    sys.exit(1)
for i in _list:
    if _list.index(i) % 2 == 0:
        print(i, end=' ')
