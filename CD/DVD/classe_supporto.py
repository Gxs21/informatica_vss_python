class supporto:
    def __init__ (self, cS, tit, aut, nB, tip, dur, aP):
        self.cod_supporto= cS
        self.titolo= tit
        self.autore= aut
        self.nr_brani= nB
        self.tipo= tip
        self.durata= dur
        self.anno_pubblicazione= aP

    def setCod_supporto (self, cS):
        self.cod_supporto = cS
    
    def setTitolo (self, tit):
        self.titolo = tit

    def setAutore (self, aut):
        self.autore = aut

    def setNr_brani (self, nB):
        self.nr_brani = nB

    def setTipo (self, tip):
        self.tipo = tip

    def setDurata (self, dur):
        self.durata = dur

    def setAnno_pubblicazione (self, aP):
        self.anno_pubblicazione = aP


        
    def getCod_supporto (self):
        return self.cod_supporto
    
    def getTitolo (self):
        return self.titolo

    def getAutore (self):
        return self.autore

    def getNr_brani (self):
        return self.nr_brani

    def getTipo (self):
        return self.tipo

    def getDurata (self):
        return self.durata

    def getAnno_pubblicazione (self):
        return self.anno_pubblicazione

    def toString (self):
        print ("il codice supporto è: ", self.cod_supporto,  "\n il titolo è: ", self.titolo, "\n l'autore è: ", self.autore, "\n il numero di brani è: ", self.nr_brani, "\n la durata è: ", self.durata, "\n l'anno di pubblicazione è: ", self.anno_pubblicazione)
