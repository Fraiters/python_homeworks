_list = input("Введите массив через пробел: ").split()
int_list = list(map(int, _list))
length_list = len(int_list)
i = 0
count = 0
isYes = False

while i < length_list - 1:
    if (int_list[i - count] <= int_list[i - count + 1]) and (count <= 1):
        isYes = True
    else:
        del int_list[i - count]
        count += 1
        isYes = False
    i += 1

if isYes:
    print("YES")
else:
    print("NO")
