class ContoBancario:
    def _init_(self,nr,n,s,np):
        self.nr_conto = nr
        self.nominativo = n
        self.saldo = 0
        self.numero_operazioni = 0

    def getNrConto(self):
        return self.nr_conto

    def getNominativo(self):
        return self.nominativo

    def setNrConto(self,nr):
        self.nr_conto=nr
    def setNominativo(self,n):
        self.nominativo=n

    def versamento(self, soldi):
        self.saldo= self.saldo + soldi
        self.numero_operazioni= self.numero_operazioni +1

    def prelievo(self, soldi):
        if(self.saldo>=soldi):
            self.saldo= self.saldo - soldi
            self.numero_operazioni=self.numero_operazioni +1
        else:
            print("non puoi farlo, mi dispiace")

    def stampa (self):
        print ('il numero di conto è: ', self.nr_conto,' il nominativo del conto è:  ',str(self.nominativo), "il saldo ammonta a: ", self.saldo, " il numero di operazioni effettuate ammonta a: ", self.numero_operazioni)