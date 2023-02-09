class punti:
    def __init__ (self, x, y):
        self.ascissa=x
        self.ordinata=y

    def getAscissa(self):
        return self.ascissa
    def getOrdinata(self):
        return self.ordinata
    def setAscissa(self,x):
        self.ascissa= x
    def setOrdinata(self, y):
        self.ordinata= y
    def disPunti (self, p_x, p_y):
        distanzaP=((self.ascissa - p_x) ^2 + (self.ordinata - p_y)^2)^(1/2)
        return distanzaP 
    def disRetta ( self, a, b, c):
        distanzaR= (a*self.ascissa + b*self.ordinata + c)/((a^2+b^2)^(1/2))
        return distanzaR
    def quadrante (self):
        if self.ascissa>0 and self.ordinata>0:
            quadrante=1
        elif self.ascissa<0 and self.ordinata>0:
            quadrante=2
        elif self.ascissa<0 and self.ordinata<0:
            quadrante=3
        else: 
            quadrante=4
        return quadrante