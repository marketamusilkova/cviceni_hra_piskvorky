import random

def tah(pole, pozice, symbol):
    return pole[:pozice] + symbol + pole[pozice + 1:]

def tah_hrace(pole, symbol_hrace):
    while True:
        pozice = int(input("Na kterou pozici (od 1 do {0}) chceš hrát? ".format(len(pole)))) - 1
        if pozice < 0:
            print("Pozice nesmí být záporná.")
        elif pozice >= len(pole):
            print("Moc velké číslo.")
        elif pole[pozice] != "-":
            print("Tato pozice je již obsazena, vyber jinou.")
        else:
            return tah(pole, pozice, symbol_hrace)

def tah_pocitace(pole, symbol_pocitace, symbol_hrace):
    for index in range(1, len(pole)):
        if pole[index] == "-":
            if pole[index - 1] == symbol_hrace:
                return tah(pole, index, symbol_pocitace)
        if pole[index] == symbol_hrace:
            if pole[index -1] == "-":
                return tah(pole, index -1, symbol_pocitace)
        if pole[index] == "-":
            if pole[index -1] == symbol_pocitace:
                return tah(pole, index, symbol_pocitace)
        if pole[index] == symbol_pocitace:
            if pole[index -1] == "-":
                return tah(pole, index-1, symbol_pocitace)

    while True:
        pozice_pocitace = random.randrange(len(pole))
        if pole[pozice_pocitace] == "-":
            return tah(pole, pozice_pocitace, symbol_pocitace)

def vyhodnot(pole):
    if "xxx" in pole:
        return "Hurá, zvítězila jsi!"
    elif "ooo" in pole:
        return "Zvítězil počítač."
    elif "-" not in pole:
        return "Remíza!"
    else:
        return None

def piskvorky1d(symbol_hrace, symbol_pocitace):
    pole = 20 * "-"
    while True:
        pole = tah_hrace(pole, symbol_hrace)
        print(pole)
        vysledek = vyhodnot(pole)
        if vysledek != None:
            print(vysledek)
            break
        pole = tah_pocitace(pole, symbol_pocitace, symbol_hrace)
        print(pole)
        vysledek = vyhodnot(pole)
        if vysledek != None:
            print(vysledek)
            break
        
piskvorky1d("x", "o")