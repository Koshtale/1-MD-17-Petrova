number = int(input("Введите количество слов которое хотите ввести:"))
cicle = 0
text = " "
while number != cicle:
    slovo = str(input("Введите слово:"))
    text = str(text + slovo)
    cicle = cicle + 1
print(text)
