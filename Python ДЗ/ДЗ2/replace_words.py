line = input("Введите строку, состоящую ровно из двух слов: ")

assert (len(line.split()) == 2), "Строка состоит не из двух слов, повторите попытку"

list_line = line.split()
list_line.reverse()
line = " ".join(list_line)

print(line)
