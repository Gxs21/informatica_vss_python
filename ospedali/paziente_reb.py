class Paziente:
#costruttore    
    def __init__(self,nl,c,n,d,cr):
        self.numeroletto=nl
        self.cognome=c
        self.nome=n
        self.diagnosi=d
        self.codicericovero=cr

#metodi
    def getnumeroletto(self):
        return self.numeroletto
    def setnumeroletto(self,numletto):
        self.numeroletto=numletto

    def getcognome(self):
        return self.cognome
    def setcognome(self,cognome):
        self.cognome=cognome
        
    def getnome(self):
        return self.nome
    def setnome(self,nome):
        self.nome=nome
        
    def getdiagnosi(self):
        return self.diagnosi
    def setdiagnosi(self,diagnosi):
        self.diagnosi=diagnosi
        
    def getcodicericovero(self):
        return self.codicericovero
    def setcodicericovero(self,codricovero):
        self.codicericovero=codricovero
        
    def toString(self):
        print("Numero Letto: "+ str(self.numeroletto))
        print("Cognome: "+ self.cognome)
        print("Nome: "+self.nome)
        print("Diagnosi: "+self.diagnosi)
        print("Codice Ricovero: "+self.codicericovero)
