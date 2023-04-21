import sys

m1, m2 = [int(i)
          for i in input().split()
          ]

n1, n2 = [int(i)
          for i in input().split()
          ]


if (m1, m2, n1, n2 <= 100) and (m1 < m2) and (n1 < n2):
    for i in range(m1, m2 + 1):
        for j in range(n1, n2 + 1):
            print(f'{i} x {j} = {i * j}')
else:
    sys.exit(1)
