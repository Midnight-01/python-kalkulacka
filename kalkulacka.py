"""
 _____ _______         _                      _
|_   _|__   __|       | |                    | |
  | |    | |_ __   ___| |___      _____  _ __| | __  ___ ____
  | |    | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / / __|_  /
 _| |_   | | | | |  __/ |_ \ V  V / (_) | |  |   < | (__ / /
|_____|  |_|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_(_)___/___|
                  ___
                 |  _|___ ___ ___
                 |  _|  _| -_| -_|  LICENCE
                 |_| |_| |___|___|

IT ZPRAVODAJSTVÍ  <>  PROGRAMOVÁNÍ  <>  HW A SW  <>  KOMUNITA

Tento zdrojový kód pochází z IT sociální sítě WWW.ITNETWORK.CZ

Můžete ho upravovat a používat jak chcete, musíte však zmínit
odkaz na http://www.itnetwork.cz
"""

def get_values():
    a = float(input("Zadejte číslo A: "))
    b = float(input("Zadejte číslo B: "))
    return a, b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Nelze dělit nulou!"
    return a / b

if __name__ == "__main__":
    a, b = get_values()
    print("Součet:", add(a, b))
    print("Rozdíl:", subtract(a, b))
    print("Součin:", multiply(a, b))
    print("Podíl:", divide(a, b))
# conflict 2
# conflict 1
