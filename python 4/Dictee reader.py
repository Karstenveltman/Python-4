import random

nieuwWoordLijst = {}
schermbreedte = 70
bestand = ""

def printWitRegel():
    print("|" + " " * (schermbreedte - 2) + "|")

def printHeader():
    print("#" + "-" * (schermbreedte - 2) + "#")

def printMenuRegel():
    print(("| {:^" + str(schermbreedte - 4)+ "} |").format("Menu"))
    
def printRegel(regel):
    print(("| {:" + str(schermbreedte - 4)+ "} |").format(regel))
    
def printFooter():
    print("#" + "-" * (schermbreedte - 2) + "#")

def kiesFile():
    printHeader()
    printRegel("Voer de naam van het txt file in.")
    printFooter()
    kiesBestand = input()
    global bestand
    bestand = kiesBestand

def nieuwBestand():
    printHeader()
    printRegel("Voer de naam van uw file in.")
    printFooter()
    nieuwBestand = input()
    open(nieuwBestand + ".txt", "w")

def nieuwWoord():
    printHeader()
    printRegel("Voer in welke key en value het nieuwe item moet hebben.")
    printFooter()
    newkey = input("1e woord: ")
    newvalue = input("2e woord: ")
    nieuwWoordLijst[newkey] = newvalue
    
    f = open(bestand + ".txt", "a")
    for item in nieuwWoordLijst:
        f.write('\n' + item+"="+nieuwWoordLijst[item])
    f.close()

def lees_woordenlijst():
    with open(bestand + ".txt") as f:
        text = f.read().split("\n")
        woordenlijst = {}
        for item in text:
            if not item == '':
                key, value = item.split("=")
                woordenlijst[key] = value
        printHeader()
        for key, value in woordenlijst.items():
            printRegel(key + " = " + value)
        printFooter()

def overhoren():
    with open(bestand + ".txt") as f:
        text = f.read().split("\n")
        woordenlijst = {}
        for item in text:
            if not item == '':
                key, value = item.split("=")
                woordenlijst[key] = value
    allKeys = []
    allValues = []

    for key, value in woordenlijst.items():
        allKeys.append(key)
        allValues.append(value)

    while True:
        keyNum = random.randint(0, (len(allKeys)-1))
        overhoorKey = allKeys[keyNum]
        overhoorValue = allValues[keyNum]
        printHeader()
        printRegel("Wat is de value van:" + "\t" + overhoorKey)
        printFooter()
        antwoord = input()
        printHeader()
        
        if antwoord == overhoorValue:
            printRegel("Goed gedaan!")
            
        else:
            printRegel("Helaas, dat is niet het goede antwoord, het goede antwoord is: \t" + quizValue)

        printRegel("Wil je doorgaan? ja of nee?")
        printFooter()
        doorgaanAntwoord = input()
        if doorgaanAntwoord == "nee":
            break

def printAfscheid():
    printHeader()
    printRegel("bye bye!")
    printFooter()

while True:
    printHeader()
    printMenuRegel()
    printWitRegel()
    printRegel("Kies tussen de volgende opties.")
    printRegel("Typ 'n' om een nieuwe lijst aan te maken")
    printRegel("Typ 'k' om een andere lijst te kiezen")
    printRegel("Typ 'v' om de gecelecteerde lijst te zien")
    printRegel("Typ 't' om een item toe te voegen aan een de lijst")
    printRegel("Typ 'o' om je te laten overhoren")
    printRegel("Typ 'q' om te stoppen")
    printWitRegel()
    printFooter()

    keuze = input()
    if keuze == "n":
        nieuwBestand()
    elif keuze == "k":
        kiesFile()
    
    elif keuze == "t":
        nieuwWoord()
        
    elif keuze == "o":
        overhoren()

    elif keuze == "v":
        lees_woordenlijst()

    elif keuze == "q":
        printAfscheid()
        break
    
    else:
        printHeader()
        printRegel("deze invoer is niet geldig.")
        printFooter()
