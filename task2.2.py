text = " "
slovo = ""
while slovo != "stop":
    slovo = str(input("Введите слово:"))
    if slovo == "stop":
        continue
    text = str(text + " " + slovo)
print(text)
