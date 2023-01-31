class Contobancario:
    def __init__(self,c,no,s,o):
        self.nr_conto=c
        self.nominativo=no
        self.saldo=s
        self.operazioni=o
    def getnr_conto (self):
        return self.nr_conto
    def getnominativo(self):
        return self.nominativo
    def getsaldo(self):
        return self.saldo
    def getoperazioni(self):
        return self.operazioni
#ora implemento i metodi set
    def setNr_conto (self,c):
        self.nr_conto=c #l'_ rende privato l'attributo
    def setNominativo (self,no):
        self.nominativo=no
    def setSaldo (self,s):
        self.saldo=s
    def setOperazioni (self,o):
        self.operazioni = o
    
    def versamento(self,da_versare):
        self.saldo += da_versare 
    def prelievo(self,da_prelevare):
        if (self.saldo>0):
            self.saldo-=da_prelevare
    def stampa_conto (self):
        print("il vostro numero di conto risulta essere: ", self.nr_conto, "il nome del vostro conto risulta essere: ", self.nominativo, "il vostro saldo risulta essere: ", self.saldo, "il numero di operazioni effettuate risulta essere: ", self.operazioni  )