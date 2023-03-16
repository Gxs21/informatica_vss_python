
from ospedale_reb import Ospedale
from paziente_reb import Paziente
def main():
    p1=Paziente(1,3, 4, 5, 6)  
    p2=Paziente(2,"Verdi","Giuseppe","Gastroenterite","Verde")
    p3=Paziente(3,"Bianchi","Francesco","Frattura omero","Giallo")
    p4=Paziente(4,"Ferrari","Luigi","Infarto","Rosso")
    p5=Paziente(5,"Rossi","Francesca","Frattura costole","Giallo")

    o1=Ospedale("Vitofazzi","Lecce")
    print(p1.numeroletto)
    o1.aggiungiPaziente(p2)
    o1.dimettiPaziente(2)   
    o1.visualizzaPazienti("verde")
    
main()