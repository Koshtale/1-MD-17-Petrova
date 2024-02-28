import random

error = 0
points = 0
otvet = 0
reshenye = 0
while error != 3:
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    reshenye = a + b
    print("Сколько будет:", a, "+", b)
    otvet = int(input(""))
    if otvet == reshenye:
        print("Правильно!")
        points += 1
    else:
        print("Ответ неверный")
        error += 1

print("Игра окончена. Правильных ответов: ", points)