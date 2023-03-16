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
    
    def modificaCodicePaziente (self, cognome):
        for i in self.listaPazienti:
            i.setCodiceRicovero(input("inserire il nuovo codice: "))
    

