
from ospedale_reb import Ospedale
from paziente_reb import Paziente
def main():
    p1=Paziente(1,"Rossi","Mario","Febbre","Bianco")
    p2=Paziente(2,"Verdi","Giuseppe","Gastroenterite","Verde")
    p3=Paziente(3,"Bianchi","Francesco","Frattura omero","Giallo")
    p4=Paziente(4,"Ferrari","Luigi","Infarto","Rosso")
    p5=Paziente(5,"Rossi","Francesca","Frattura costole","Giallo")

    o1=Ospedale("Vitofazzi","Lecce")
 
    o1.dimettiPaziente(p2)   