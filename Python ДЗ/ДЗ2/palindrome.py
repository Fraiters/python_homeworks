K = int(input("Введите число K (1 ≤ K ≤ 100 000) = "))
count_palindrome = 0

assert (1 <= K <= 100000), "Число введено некорректно, повторите попытку"

for index in range(1, K + 1):
    line = str(index)

    if line == line[::-1]:
        count_palindrome += 1

print(count_palindrome)