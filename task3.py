year = int(input("Введите год:"))
if (year % 4 == 0) and (year % 100 != 100) or (year % 400 == 0):
    print("Год ", year, " - високосный")
else:
    print("Этот год не високосный.")