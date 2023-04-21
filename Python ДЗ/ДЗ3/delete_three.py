line = input("Введите строку: ")

list_line = list(line)
index = 0
count = 0
length = len(list_line)

while index < length:
    if index % 3 == 0:
        del list_line[index - count]
        count += 1
    index += 1

print("".join(list_line))
