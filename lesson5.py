def na7(number):
    if number % 7 == 0:
        print("Число ", number, " делится на 7.")
    else:
        print("Число ", number, " не делится на 7.")
def dvesty(number):
    res = 200 / number
    print("Ответ равен:", res)
def truefalse():
    date = str(input("Введите дату:"))
    aaa = date.split('.')
    if int(aaa[0]) * int(aaa[1]) != int(aaa[2]):
        print("Число не магическое")
        return True
    else:
        print("Число магическое")
        return False

def ticket():
    ticknumber = str(input("Введите номер билета:"))
    firstthree = ticknumber[:3]
    lastthree = ticknumber [3:]
    summfirst = 0
    summlast = 0
    for x in firstthree:
        summfirst +=  int(x)
    for x in lastthree:
        summlast += int(x)
    if summfirst == summlast:
        print("Номер ", ticknumber , " - счастливый")
    else:
        print("Номер ", ticknumber, " - не счастливый")

taskk = int(input("Какую задачу решить?"))
match taskk:
    case 1:
        number = int(input("Введите число:"))
        na7(number)
    case 2:
        number = int(input("Введите число:"))
        dvesty(number)
    case 3:
        truefalse()
    case 4:
        ticket()
    case _:
        print("Такой задачи нет.")