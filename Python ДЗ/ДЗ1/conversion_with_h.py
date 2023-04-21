line = input("Введите строку, в которой буква h встречается как минимум два раза: ")
assert (line.count('h') >= 2), "ERROR"

begin = line[:line.find('h')]
mid = line[line.find('h'):line.rfind('h') + 1]
end = line[line.rfind('h') + 1:]
line = begin + mid[::-1] + end

print(line)
