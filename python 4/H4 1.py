def lees_woordenlijst(bestandsnaam):
    with open(bestandsnaam) as f:
        text = f.read().split("\n")
        woordenlijst = {}
        for item in text:
            if not item == '':
                key, value = item.split("=")
                woordenlijst[key] = value
        return woordenlijst

print(lees_woordenlijst("H4text.txt"))
