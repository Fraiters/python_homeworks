import sys


def dist2(k, j):
    return sum([(k[i] - j[i]) ** 2 for i in range(1, len(k))])


n = int(input())
m = int(input())

if (2 <= n <= 100) and (1 <= m <= 20):
    points = [
        [(lambda x: int(x) if x.isdigit() else x)(i)
         for i in input().split()
         ] for i in range(m)
    ]

    for a in range(m):
        for b in range(m):
            for c in range(a, m):
                if len({a, b, c}) != 3:
                    continue

                if dist2(points[a], points[c]) == dist2(points[b],
                                                        points[c]) + dist2(points[a], points[b]):
                    print(points[a][0], points[b][0], points[c][0])
else:
    sys.exit(1)
