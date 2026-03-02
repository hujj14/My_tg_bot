def Parser(datafromDB):
    book = {
        "M" : "Математика",
        "I" : "IT",
        "F" : "Физика",
        "F|2" : "Физика",
        "M|2" : "Математика",
        "A|J" : "Англиский c J",
        "A|M" : "Английский с М"
    }
    fin = []
    if datafromDB is None :
        return "Сегодня занятий нет"
    for i in datafromDB.split(","):
        originalstr = ""
        zzzz = i.index("-")
        if zzzz == 1:
            originalstr += book[i[0]]
        elif zzzz > 1:
            originalstr += book[i[:3]]
        originalstr += " "
        originalstr += i[-5:]
        fin.append(originalstr)
    print(fin)
    return fin

Parser("A|J-19:00,I-21:00")
