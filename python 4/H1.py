schermbreedte = 70

def printHeader():
    print("-" * schermbreedte)
    print(" " * schermbreedte)
    
def printRegel(regel):
    print(("> Je gekozen woord: {:>" + str(schermbreedte - 22)+ "} <").format(regel))
    
def printFooter():
    print(" " * schermbreedte)
    print("-" * schermbreedte)

woord1 = input()
woord2 = input()
woord3 = input()
printHeader()
printRegel(woord1)
printRegel(woord2)
printRegel(woord3)
printFooter()
