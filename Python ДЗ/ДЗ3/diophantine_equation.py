import sys

try:
    list_value = input("Введите параметры a, b, c, d, e соответственно: ").split()
    int_list = list(map(int, list_value))
except ValueError:
    sys.exit(1)

try:
    a = int_list[0]
    b = int_list[1]
    c = int_list[2]
    d = int_list[3]
    e = int_list[4]
except IndexError:
    sys.exit(1)

solution = 0

for x in range(1001):
    if x != e and (a * x ** 3 + b * x ** 2 + c * x + d) == 0:
        solution += 1

print(solution)
