def slovar():
    dictionary = {'Россия':'Москва','Нидерланды':'Амстердам','Германия':'Берлин','Греция':'Афины','Словакия':'Братислава','Румыния':'Бухарест','Польша':'Варшава','Австрия':'Вена','Украина':'Киев','Дания':'Копенгаген','Великобритания':'лондон','Испания':'Мадрид','Чехия':'Прага'}
    list_keys = list(dictionary.keys())
    print('Все пары: ')
    for i in list_keys:
        print(i, ':', dictionary[i])
    print('')
    print('Столица Нидерландов: ')
    print(dictionary['Нидерланды'])
    print('')
    print('Все пары в алфавитном порядке: ')
    list_keys.sort()
    for i in list_keys:
        print (i, ':', dictionary[i])
def erudit():
    odin = {'а','в','е','и','н','о','р','с','т'}
    dva = {'д', 'к', 'л', 'м', 'п', 'у'}
    tri = {'б', 'г', 'ё', 'ь', 'я'}
    chetyre = {'й', 'ы'}
    pyat = {'ж', 'з', 'х', 'ц', 'ч'}
    vosem = {'ш', 'э', 'ю'}
    desyat = {'ф','щ','ъ'}

    cena = 0
    slovo = (str(input('Введите слово: ')))
    chasty = list(slovo)
    for chasty in slovo:
        if chasty in odin:
            cena += 1
        if chasty in dva:
            cena += 2
        if chasty in tri:
            cena += 3
        if chasty in chetyre:
            cena += 4
        if chasty in pyat:
            cena += 5
        if chasty in vosem:
            cena += 8
        if chasty in desyat:
            cena += 10
    else:
        cena += 0
    print('Слово ', slovo, ' стоит ', cena, '.')

def dop():
    Chinese = {'Мустафа','Чжао','Янь','Владимир','Беатрис'}
    Russian = {'Мустафа','Петр','Анастасия','Владимир','Янь','Алиса','Марк','Полина','Беатрис','Чжао'}
    English = {'Петр','Алиса','Марк'}
    Spanish = {'Мустафа','Петр','Анастасия','Владимир','Янь'}


taskk = int(input("Какую задачу решить? "))
match taskk:
    case 1:
        slovar()
    case 2:
        erudit()
    case 3:
        dop()
    case _:
        print("Такой задачи нет.")