import sys


def countSort(a):
    largest = max(a)
    store_list = [0] * (largest + 1)

    for index in range(len(a)):
        store_list[a[index]] = store_list[a[index]] + 1

    store_list[0] = store_list[0] - 1

    for index in range(1, largest + 1):
        store_list[index] = store_list[index] + store_list[index - 1]

    result = [None] * len(a)

    for index in reversed(a):
        result[store_list[index]] = index
        store_list[index] = store_list[index] - 1

    return result


try:
    unsorted_list = input("Введите элементы списка через пробел от 0 до 100 "
                          "(кол-во эл-в N <= 2 * 10 ** 5): ").split()
    int_unsorted_list = list(map(int, unsorted_list))

    if len(int_unsorted_list) > (2 * (10 ** 5)):
        sys.exit("ERROR!")

    for i in range(len(unsorted_list)):
        if (int_unsorted_list[i] < 0) or (int_unsorted_list[i] > 100):
            sys.exit("ERROR!")

except ValueError:
    sys.exit("ERROR!")

sorted_list = countSort(int_unsorted_list)

for i in range(len(sorted_list)):
    print(sorted_list[i], end=" ")
