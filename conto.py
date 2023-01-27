class Conto:
    def __init__ (self,nr_conto, nom, sal, numOp):
        self.numeroConto = nr_conto
        self.nominativo = nom
        self.saldo = sal
        self.numOper = numOp

    def getNumeroConto (self):
        return self.numeroConto
    def getNominativo (self):
        return self.nominativo
    def getSaldo (self):
        return self.saldo
    def getNum_Oper (self):
        return self.numOper

    def setNumeroConto(self, nr_conto):
        self.numeroConto = nr_conto
    
    def setNominativo(self, nom):
        self.nominativo = nom
   
    def setSaldo(self, sal):
        self.saldo = sal

    def setNumerOper(self, numOp):
        self.numeroConto = numOp

    def versamento (self, vers):
        self.saldo+=vers
        self.numOper+=1

    def prelievo (self, prel ):
        if (self.saldo > 0) :
            self.saldo-=prel
        self.numOper+=1
    def visualizza (self):
        print ('Numero Conto', self.numeroConto,' Nominativo ',self.getNumeroConto())