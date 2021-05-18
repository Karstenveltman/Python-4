def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    f = open(bestandsnaam, "w")
    for item in woordenlijst:
        f.write(item+"="+woordenlijst[item]+'\n')
    f.close()

woordenlijst = { "koe": "cow", "schaap": "sheep", "varken": "pig" }
schrijf_woordenlijst("nl-en.txt", woordenlijst)
