class ContoBancario:
    def __init__(self,nr_conto,nominativo,saldo=0):
        self.nr_conto=nr_conto
        self.nominativo=nominativo
        self.saldo=saldo
        self.num_operazioni=0

    def versamento(self,importo):
        self.saldo += importo
        self.num_operazioni +=1
    def prelievo(self,importo):
        if self.saldo >=importo:
            self.saldo -=importo
            self.num_operazioni+=1
        else:
            print("saldo insufficiente")
    def visualizza(self):
            print("nr conto:",self.nr_conto)
            print("nominativo:",self.nominativo)
            print("saldo:", self.saldo)
            print("numero operazioni:", self.num_operazioni)
    def _str_(self):
        return f"nr conto:{self.nr_conto}, nominativo:{self.nominativo}, saldo:{self.saldo},numero operazioni{self.num_operazioni}"
    def set_nr_conto(self,nr_conto):
            self.nr_conto=nr_conto
    def set_nominativo(self,nominativo):
            self.nominativo=nominativo
    def set_saldo(self,saldo):
            self.saldo=saldo
    def set_num_operazioni(self,num_operazioni):
            self.num_operazioni=num_operazioni
    def get_nr_conto(self):
            return self.nr_conto
    def get_nominativo(self):
            return self.nominativo
    def get_saldo(self):
            return self.saldo
    def get_num_operazioni(self):
            return self.num_operazioni