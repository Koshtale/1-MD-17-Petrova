colour1 = input("Выбор первого цвета:")
if colour1 == 'красный':
    colour1 = 1
if colour1 == "синий":
    colour1 = 2
if colour1 == "желтый":
    colour1 = 3
else:
    print("Введите один из основных цветов.")
colour2 = input("Выбор второго цвета:")
if colour1 == colour2:
    print("Вы должны выбрать разные цвета.")
else:
    final = colour1 + colour2
    if final == 3:
        print ("Фиолетовый")
    if final == 4:
        print("Оранжевый")
    if final == 5:
        print("Зеленый")
    else:
        print("Ошибка")