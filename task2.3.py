slovo = ""
while slovo != "stop":
    slovo = str(input("Введите слово:"))
    redko = "ф"
    if slovo == "stop":
        continue
    if redko in slovo:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")