A = int(input("Введите число A: "))
B = int(input("Введите число B (должно быть меньше числа A): "))

assert (A > B), "Число A не больше числа B, повторите попытку"

operation_division = ":2"
operation_subtraction = "-1"

while (A != B):

    if ((A // 2 >= B) and (A % 2 == 0)):
        A /= 2
        print(operation_division)
    else:
        A -= 1
        print(operation_subtraction)
