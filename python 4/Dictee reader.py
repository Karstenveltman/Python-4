schermbreedte = 70

def printWitRegel():
    print("|" + " " * (schermbreedte - 2) + "|")

def printHeader():
    print("#" + "-" * (schermbreedte - 2) + "#")
    print(("| {:^" + str(schermbreedte - 4)+ "} |").format("Menu"))
    printWitRegel()
    
def printRegel(regel):
    print(("| {:" + str(schermbreedte - 4)+ "} |").format(regel))
    
def printFooter():
    print("#" + "-" * (schermbreedte - 2) + "#")


printHeader()
printRegel("Kies tussen de volgende opties.")
printRegel("Typ 'n' om een nieuwe lijst aan te maken")
printRegel("Typ 'k' om een andere lijst te kiezen")
printRegel("Typ 'v' om de huidige lijst te laten zien")
printRegel("Typ 't' om een item toe te voegen aan een de lijst")
printRegel("Typ 'd' om een item te verwijderen uit de lijst")
printRegel("Typ 'o' om je te laten overhoren")
printRegel("Typ 'w' om de lijst op te slaan")
printRegel("Typ 'q' om te stoppen")
printFooter()
