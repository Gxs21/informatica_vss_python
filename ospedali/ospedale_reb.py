class Ospedale:
#costruttore    
    def __init__(self,nOspedale,c):
            self.nomeospedale=nOspedale
            self.citta=c
            self.capienzamassima=20
            self.listapazienti=list()
   
#metodi
    def setNomeospedale (self, nOspedale):
        self.nomeospedale=nOspedale
    def setCitta (self, c):
        self.citta=c
    def setCapienzamassima (self):
        self.listapazienti=20
    def setListapazienti (self):
        self.listapazienti=list()
    def getNomeospedale (self):
        return self.nomeospedale
    def getCitta (self):
        return self.citta
    def getNomeospedale (self):
        return self.nomeospedale
    def getListapazienti (self):
        return self.listapazienti
    def visualizzaPazienti (self):
        for x in self.listapazienti:
            x.toString()

    def aggiungiPaziente (self,p):
        size=len(self.listapazienti)
        if size<self.capienzamassima:
            self.listapazienti.append(p)
            print("IL PAZIENTE E' STATO AGGIUNTO")
        else:
            print("L'OSPEDALE E' PIENO")
            
    def modificaCodicePaziente(self,c,cr):
        Trovato="no"
        for x in self.listapazienti:
            if x.getcognome()==c:    
                x.setcodicericovero(cr) 
                Trovato="si"
            if Trovato=="no":
                print("IL PAZIENTE NON ESISTE")
        
    def dimettiPaziente(self,nl):
        Trovato=False
        for x in self.listapazienti:
            if x.getnumeroletto()==nl:
                Trovato=True
                self.listapazienti.remove(x)
            if Trovato==True:
                print("IL PAZIENTE E' STATO DIMESSO")
            else:
                print("IL PAZIENTE NON ESISTE")
                
    def visualizzaPazienti(self,cr):
        for x in self.listapazienti:
            if x.getcodicericovero()==cr:
                x.toString()

