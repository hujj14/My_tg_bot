def Parser(datafromDB):
    book = {
        "M" : "Математика",
        "I" : "IT",
        "F" : "Физика",
        "A|J" : "Англиский c J",
        "A|M" : "Английский с М"
    }

    originalstr = ""

    zzzz = datafromDB.index("-")
    if zzzz == 1:
        originalstr += book[datafromDB[0]]
    elif zzzz > 1:
        originalstr += book[datafromDB[:3]]

    originalstr += " "
    originalstr += datafromDB[-5:]
    return originalstr


