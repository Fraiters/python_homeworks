import sys

summa = 0
try:
    n = int(input("Натуральное число >= 2: "))
    if n < 2:
        sys.exit(1)
    for i in range(1, n):
        print(f"{i}*{i + 1}", end="+" if i < n - 1 else "=")
        summa += i * (i + 1)
    print(summa)
except ValueError:
    sys.exit(1)
