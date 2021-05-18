woordenlijst = {}

def addItem(woordenlijst):
    newkey = input("Woord 1: ")
    newvalue = input("Woord 2: ")
    woordenlijst[newkey] = newvalue
    print(woordenlijst)
while True:
    addItem(woordenlijst)
    stoppen = input("wil je stoppen? ")
    if stoppen == "ja":
        break
    

    
