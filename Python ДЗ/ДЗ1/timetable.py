number_lesson = int(input("Введите номер урока (от 1 до 10): "))

assert (1 <= number_lesson <= 10), "ERROR"

number_lesson = number_lesson * 45 + (number_lesson // 2) * 5 + ((number_lesson + 1) // 2 - 1) * 15

hour = number_lesson // 60 + 9
minute = number_lesson % 60

print(hour, minute)
