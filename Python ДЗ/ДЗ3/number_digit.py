import sys

try:
    n = [0] * 10
    while True:
        n[int(input("Введите число n (0 <= n <= 9): "))] += 1
        if n[0]:
            break
    print(*n[1:])

except ValueError:
    sys.exit(1)
