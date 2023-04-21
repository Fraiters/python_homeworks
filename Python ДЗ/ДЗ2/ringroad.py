v = int(input("Введите скорость v = "))
t = int(input("Введите время t = "))
way_length = 109

assert ((-1000 < v < 1000) and (0 <= t < 1000))

if v >= 0:
    stop_point = v * t % way_length
    print(stop_point)
else:
    stop_point = v * t % way_length
    print(stop_point)
