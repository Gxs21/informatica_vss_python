class ospedale:
    def __init__(self, nomO, cit, cmax):
        self.nomeOspedale=nomO
        self.citta=cit
        self.capienzaMassima=cmax
        self.listaPazienti=list()

    def setNomeOspedale(self, nomO):
        self.nomeOspedale=nomO

    def setCitta(self, cit):
        self.citta=cit

    def setCapienzaMassima(self, cmax):
        self.capienzaMassima=cmax

    def setListaPazienti(self):
        self.listaPazienti=list()

    def getNomeOspedale (self):
        return self.nomeOspedale 

    def getCitta (self):
        return self.citta

    def getCapienzaMassima (self):
        return self.capienzaMassima
    
    def getListaPazienti(self):
        return self.listaPazienti
    
    def visualizzaPazienti (self):
        for i in self.listaPazienti:
            i.toString()

    def aggiungiPazienti (self, p):
        if len(self.listaPazienti)<self.capienzaMassima:
            self.listaPazienti.append (p)
            print (" il paziente è stato aggiunto con successo")
    
    def modificaCodicePaziente (self, cognome):
        for x in self.listaPazienti:
            if x.getCognome == cognome:
                x.setCodiceRicovero(input("inserire il nuovo codice: "))
                print ("il nuovo codice paziente è:" + x.getCodiceRicovero)
    def dimettiPaziente (self,numLetto):
        for i in self.listaPazienti:
            if i.getNumeroLetto==numLetto:
                self.listaPazienti.erase(i)
                print ("il paziente è stato dimesso con successo")
    
    def visualizzaPaziente (self, cR):
        for i in self.listaPazienti:
            if i.getCodiceRicovero == cR:
                i.toString()
                
    

