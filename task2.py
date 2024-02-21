number = int(input("Введите номер места:"))
if number ==0 or number>54:
    print("Такого места нет.")
if number>=38:
    print("У вас боковое место.")
if number<38 and (number%2 == 0):
    print("У вас верхнее место.")
if number<38 and (number%2 != 0):
    print("У вас нижнее место.")