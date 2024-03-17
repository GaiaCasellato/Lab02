import re
class Dictionary:
    def __init__(self, dizionario = {}):
        self._dizionario = dizionario


    def addWord(self, input_utente):
        if len(input_utente)== 2:
            if input_utente[0] not in self._dizionario: # controllo che la parola inserita dall'utente non sia già nel mio dizionario
                self._dizionario[input_utente[0]]= input_utente[1] # aggiungo la nuova parola con il suo significato nel dizionario
            else: # altrimenti se sono più traduzioni associate ad una nuova parola devo fare in modo di aggiungerle tutte
                traduzione_precedente = self._dizionario.get(input_utente[0]) #prendo la traduzione già presente per quella parola passata dall'utente
                if isinstance(traduzione_precedente,str):
                    traduzioni = []
                    traduzioni.append(traduzione_precedente)
                else:
                    traduzioni = self._dizionario.get(input_utente[0])
                    print(traduzioni)
                    self._dizionario[input_utente[0]] = [*traduzioni, input_utente[1]]
                    print(self._dizionario[input_utente[0]])


    def translate(self,parola_aliena):
        return self._dizionario[parola_aliena]
    def translateWordWildCard(self,wildCard):
        wildCard = wildCard.replace("?",".")
        print(wildCard)
        matchCounter = 0
        sb = []

        for w in self._dizionario.keys():
            if re.search(wildCard,w):
                matchCounter += 1
                sb.append(self._dizionario.get(w))

        if matchCounter != 0:
            return sb
        else:
            return None

    def loadDictionary(self):
        file_path = 'dictionary.txt'

        with open(file_path,'r') as file:
            for line in file:
                input = line.strip().split()
                if len(input) == 2:
                    self._dizionario[input[0]]= input[1]


    def printAll(self):
        for chiave,valore in self._dizionario.items():
            parola_aliena = chiave
            traduzione = valore
            print(f"Parola aliena: {parola_aliena}, Traduzione: {traduzione}\n")