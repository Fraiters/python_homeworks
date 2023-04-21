line = ' ' + input()
n = len(line)
res = []
i = 0

while i < n:
    if line[i] == ' ':
        res.append('')

    if line[i] == '"':
        i += 1
        while line[i] != '"':
            res[-1] += line[i]
            i += 1

    if line[i].isalpha() or line[i] == "'":
        res[-1] += line[i]

    if line[i] == '-':
        if line[i - 1] != ' ':
            if line[i + 1].isalpha():
                res[-1] += '-'
            else:
                res.append('')
                while line[i + 1] == '-':
                    i += 1
        else:
            i += 1
            while line[i].isalpha() or line[i] in "'-":
                if line[i] == '-':
                    res.append('')
                else:
                    res[-1] += line[i]
                i += 1

    i += 1

for elem in range(len(res)):
    print(res[elem], end='')
    if res[elem] != res[-1]:
        print(',', end='')

print(end='.')
