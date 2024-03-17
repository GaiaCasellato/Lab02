import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()
    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?\n")
        str = input()
        str.lower()
        t.handleAdd(str)
        print("Aggiunta!")

    if int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?\n")
        str = input()
        print(t.handleTranslate(str))
        continue
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?\n")
        txtIn = input()
        txtTrans1= t.handleWildCard(txtIn)
        print(txtTrans1)
    if int(txtIn) == 4:
        t.printAll()
    if int(txtIn) == 5:
        break