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


