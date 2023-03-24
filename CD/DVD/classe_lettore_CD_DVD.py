class lettore:
    def __init__ (self, nC, dM):
        self.nome_collezione = nC
        self.dim_max = dM
        self.lista_CD_DVD = []

    def setNome_collezione (self, nC):
        self.nome_collezione = nC

    def setDim_max (self, dM):
        self.dim_max = dM

    def setLista_CD_DVD (self):
        self.lista_CD_DVD= []

    def getNome_collezione (self):
        return self.nome_collezione
    
    def getDim_max (self):
        return self.dim_max
    
    def getLista_CD_DVD (self):
        return self.lista_CD_DVD
    
    def add_supporto (self, s):
        if len(self.lista_CD_DVD) < self.dim_max:
            self.lista_CD_DVD.append(s)
            print("il supporto è stato aggiunto con successo alla collezione!")
        else:
            print ("la collezione è piena!")

    def get_nr_CD_DVD(self):
        if len(self.lista_CD_DVD) != 0:
            return len(self.lista_CD_DVD)
        else: 
            return -1
        
    def add_to_pos(self, s, pos):
        if len(self.lista_CD_DVD) < self.dim_max:
            self.lista_CD_DVD.insert(pos, s)
            return "il supporto è stato inserito correttamente nella collezione!"
        else:
            return "la collezione è piena!"
        
    def kill_supporto (self, codice):
        for s in self.lista_CD_DVD:
            if s.getCod_supporto() == codice:
                self.lista_CD_DVD.remove(s)
                print ("il supporto è stato rimosso correttamente dalla collezione!")
                return True
            else:
                print("il supporto non è stato trovato all'interno della collezione!")
                return False

    def cerca_supporto(self, titolo):
        for s in self.lista_CD_DVD:
            if s.getTitolo() == titolo:
                print ("il supporto è stato trovato all'interno della collezione!")
                return s
            else:
                return False
        
    def visualizza_supporti (self, autore):
        for s in self.lista_CD_DVD:
            if s.getAutore() == autore:
              s.toString()
            else:
                return False
            
    def visualizza_collezione (self):
        for s in self.lista_CD_DVD:
            s.toString()
        if len(self.lista_CD_DVD) == 0:
            print ("collezione vuota")
     
        



