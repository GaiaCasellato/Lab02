from dictionary import Dictionary


class Translator:

    def __init__(self, dizionario = Dictionary()):
        self._dizionario = dizionario
        pass

    def printMenu(self):
        print("-----------------------------")
        print("  Translator Alien-Italian")
        print("-----------------------------")
        print("1. Aggiungi nuova parola \n"
         "2. Cerca una traduzione \n"
         "3. Cerca con wildcard \n"
         "4. Stampa tutto il dizionario\n"
         "5. Exit")
        print("-----------------------------")


    def loadDictionary(self, txtEntry):
        # dict is a string with the filename of the dictionary
        self._dizionario.loadDictionary()


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        input = entry.split(" ")
        print(input)
        self._dizionario.addWord(entry)

    def handleTranslate(self, query):
        return self._dizionario.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self._dizionario.translateWordWildCard(query)

    def printAll(self):
        self._dizionario.printAll()