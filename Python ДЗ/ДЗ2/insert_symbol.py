line = input("Введите строку: ")
symbol = '*'
newline = ""

for letter in line:
    newline += letter + symbol

newline = newline[::-1].replace(symbol, '', 1)
newline = newline[::-1]

print("Новая строка: ", newline)
