
from ospedale_reb import Ospedale
from paziente_reb import Paziente
def main():
    p1=Paziente("uno",3, 4, 5, 6)  
    p2=Paziente(2,"Verdi","Giuseppe","Gastroenterite","Verde")
    p3=Paziente(3,"Bianchi","Francesco","Frattura omero","Giallo")
    p4=Paziente(4,"Ferrari","Luigi","Infarto","Rosso")
    p5=Paziente(5,"Rossi","Francesca","Frattura costole","Giallo")

    o1=Ospedale("Vitofazzi","Lecce")
    
    o1.aggiungiPaziente(p2)
    o1.aggiungiPaziente(p3)
    o1.aggiungiPaziente(p4)
    o1.aggiungiPaziente(p5)
    o1.modificaCodicePaziente("Verdi", "Blu")
    o1.visualizzaPaziente("Blu")
    
    o1.dimettiPaziente(3)
    """o1.dimettiPaziente(2)"""
    
main()