from conto import Conto

def main():
    select=0
    sal=-1
    nr_conto= int(input("inserire il numero di conto"))
    nom= input ("inserire il nome del conto")
    conto= Conto (nr_conto, nom, sal, 0)
    

    while sal>=0:
        sal= int(input("inserire il saldo iniziale"))
    while (select!=1 and select != 2): 
        select=int(input("digitare: 1 per eseguire un versamento \n digitare 2 per eseguire un prelievo"))

    if (select==1):
        vers=-1
        while (vers<0):
            vers=int(input("inserire la somma da versare"))
        Conto.versamento(vers)
    if (select==2):
        prel=-1
        while (prel<0):
            prel=int(input("inserire la somma da versare"))
        Conto.prelievo(prel)
    print(conto.visualizza())
main()