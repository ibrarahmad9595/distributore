from model.Bibita import Bibita
from model.Tessera import Tessera
from model.Colonna import Colonna

class Distributore:
    def __init__(self,bibita):
        self.bibita = bibita
        self.bibita_lista = []
        self.credit_lista = []
        self.colonna_lista = []

    def aggiungiBevanda(self, codice, nome, prezzo):
        print("************************** aggiungiBevanda Method **************************")
        add_bevanda = Bibita(codice, nome, prezzo)
        self.bibita_lista.append(add_bevanda);
        print("Following new record is added")
        print("Codice: {}, Nome: {}, Prezzo: {}\n".format(codice, nome, prezzo))

    def getPrice(self, codiceBibita):
        print("************************** getprice Method **************************")
        found = None
        for x in self.bibita_lista:
            if x.codice==codiceBibita:
                print("Yes, Record is found. Following is the details")
                print("Codice: {}, Nome: {}, Prezzo: {}\n".format(x.codice, x.nome, x.prezzo))
                found = "yes"
                break
        if found!="yes":
            raise Exception("BevandaNonValida")

    def getNome(self, codiceBibita):
        print("************************** getnome Method **************************")
        found = None
        for x in self.bibita_lista:
            if x.codice==codiceBibita:
                print("Yes, Record is found. Following is the details")
                print("Codice: {}, Nome: {}, Prezzo: {}\n".format(x.codice, x.nome, x.prezzo))
                found = "yes"
                break
        if found!="yes":
            raise Exception("BevandaNonValida")

    def caricaTessera(self, codiceTessera, credito):
        print("************************** caricaTessera Method **************************")
        credit = Tessera(codiceTessera, credito)
        self.credit_lista.append(credit)
        print("Following new record is added")
        print("Codice: {}, Credito: {}\n".format(codiceTessera, credito))


    def leggiCredito(self, codiceTessera):
        print("************************** leggiCredito Method **************************")
        found = None
        for x in self.credit_lista:
            if x.codiceTessera == codiceTessera:
                print("Yes, Record is found. Following is the details")
                print("Codice: {}, Credito: {}\n".format(x.codiceTessera, x.credito))
                found = "yes"
                break
        if found != "yes":
            raise Exception("TesseraNonValida ")

    def aggiornaColonna(self, nomeBibita, numeroLattine):
        print("************************** aggiornaColonna Method **************************")
        add_colonna = Colonna(nomeBibita, numeroLattine)
        self.colonna_lista.append(add_colonna);
        print("Following new record is added")

        print("Numero Colonna: {}, Numero Colonna: {}, Numero Lattine: {}\n".format(len(self.colonna_lista), nomeBibita, numeroLattine))

    def erogaBibita(self, codiceBibita, codiceTessera):
        print("************************** erogaBibita Method **************************")
        codice_bibita = None
        codice_tessera = None
        cred = None
        prez = None
        for x in self.bibita_lista:
            if codiceBibita in x.codice:
                print("codiceBibita Found")
                prez = x.prezzo
                codice_bibita = "Found"

        for y in self.credit_lista:
            if str(codiceTessera) in str(y.codiceTessera):
                print("codiceTessera Found")
                cred = y.credito
                codice_tessera = "Found"

        if codice_bibita=="Found" and codice_tessera=="Found":
            if cred>=prez:
                canFlag = self.checkCan()
                for can in self.colonna_lista:
                    if can.nomeBibita[0] == codiceBibita and can.numeroLattine>=1:    # compare codice e.g. A and Can numbers
                        print("Before--> Nome Bobota:{} Numero Lattine: {}".format(can.nomeBibita,can.numeroLattine))
                        can.numeroLattine = can.numeroLattine - 1
                        print("After--> Nome Bobota:{} Numero Lattine: {}".format(can.nomeBibita,can.numeroLattine))
                        for y in self.credit_lista:
                            if str(codiceTessera) in str(y.codiceTessera):
                                print("Before--> Codice Tessera:{} Credito: {}".format(y.codiceTessera,
                                                                                          y.credito))
                                cred = y.credito
                                y.credito = y.credito - prez
                                print("Before--> Codice Tessera:{} Credito: {}".format(y.codiceTessera,
                                                                                       y.credito))
            else:
                raise Exception("CreditoInsufficiente")

    def checkCan(self):
        zero = 0
        for x in self.colonna_lista:
            if  str(x.numeroLattine)==str(0):
                zero = zero + 1
                if str(len(self.colonna_lista))==str(0):
                    print("throw exception zero value")
                    raise Exception("BevandaEsaurita")



