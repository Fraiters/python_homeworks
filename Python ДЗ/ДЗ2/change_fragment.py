line = input("Введите строку: ")
old_symbol = 'h'
new_symbol = "H"

line = line.replace(old_symbol, new_symbol, line.count(old_symbol)-1)
line = line.replace(new_symbol, old_symbol, 1)

print(line)