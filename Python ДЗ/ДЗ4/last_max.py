import sys

try:
    _list = input("Введите элементы списка через пробел: ").split()
    int_list = list(map(int, _list))
except ValueError:
    sys.exit("ERROR!")

max_elem = 0
index_max = 0

for i in range(len(int_list)):
    if int_list[i] >= max_elem:
        max_elem = int_list[i]
        index_max = i

print(max_elem, index_max)
