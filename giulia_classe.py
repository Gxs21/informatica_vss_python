class Contobancario:
    def __int__(self,c,no,s,o):
     self.nr_conto=c
     self.nominativo=no
     self.saldo=s
     self.operazioni=o
    def getnr_conto (self,c):
        return self.nr_conto
    def getnominativo(self,no):
        return self.nominativo
    def getsaldo(self,s):
        return self.saldo
    def getoperazioni(self,o):
        return self.operazioni
#ora implemento i metodi set
    def setNr_conto (self,c):
        self._nrconto=c #l'_ rende privato l'attributo
    def setNominativo (self,no):
        self._nominativo=no
    def setSaldo (self,s):
        self._saldo=s
    def setOperazioni (self, o):
        self._operazioni += 1
    
    def versamento(self,da_versare):
        self._saldo+= da_versare 
    def prelievo(self,da_prelevare):
        if saldo<0:
        self._saldo-= da_prelevare