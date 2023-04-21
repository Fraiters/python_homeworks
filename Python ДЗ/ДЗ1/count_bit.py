number = int(input("Введите натуральное число меньше 16: "))

assert ((number <= 0) or (number < 16)), "Число не натуральное либо не меньше 16, повторите попытку"

bin_number = bin(number)
string_bin_number = str(bin_number)

count_bit_one = string_bin_number.count('1')

print(count_bit_one)
