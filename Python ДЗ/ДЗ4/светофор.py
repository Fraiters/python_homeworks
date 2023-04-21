import sys

i = int(input())

if 1 <= i <= 100:
    if i == 1:
        print(1, 1)
    else:
        print(i, 2 * i - 1)
else:
    sys.exit(1)
