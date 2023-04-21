count_words = 0
len_string = 10

print("Введите 10 слов, (каждое слово на новой строке): ")

for index in range(len_string):
    line = input()

    assert (line != ""), "Строка пустая, повторите попытку"

    if (line[0] == 'S' or line.find('i') != -1 or len(line) == 6):
        count_words += 1

print(count_words)
