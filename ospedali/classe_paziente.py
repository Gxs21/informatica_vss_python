class paziente:
    def __init__ (self, nL, c, n, d, cR):
        self.numLetto= nL
        self.cognome=c
        self.nome= n
        self.diagnosi=d
        self.codiceRicovero=cR
    
    def setNumeroLetto (self, nL):
        self.numLetto= nL

    def setCognome (self, c):
        self.cognome= c
    
    def setNome (self, n):
        self.nome= n
    
    def setDiagnosi (self, d):
        self.diagnosi=d
    
    def setCodiceRicovero (self, cR):
        self.codiceRicovero= cR
    
    

    def getNumeroLetto (self):
        return self.numLetto
    
    def getCognome (self):
        return self.cognome
    
    def getNome (self):
        return self.nome
    
    def getDiagnosi (self):
        return self.diagnosi
    
    def getCodiceRIcovero (self):
        return self.codiceRicovero
    
    def toString(self):
        print("Numero Letto: "+str(self.numLetto))
        print("Cognome: "+str(self.cognome))
        print("Nome: "+str(self.nome))
        print("Diagnosi: "+str(self.diagnosi))
        print("Codice Ricovero: "+str(self.codiceRicovero))
