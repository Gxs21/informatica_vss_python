from giulia_classe import Contobancario
def main():
    nr_conto=int(input ("inserire il numero del conto: "))
    nominativo=input ("inserire il suo nominativo: ")
    saldo=int(input("iserisci il saldo attuale: "))
    conto = Contobancario (nr_conto, nominativo, saldo, 0)
    while True:
        n=str(input("per prelevare inserisci:  p , per versare v: "))
        if n=="p":
            Prelievo=int(input("inserisci la somma he vuoi prelevare"))
        if Prelievo<conto.saldo:
            conto.prelievo (Prelievo,)
        if n=="v":
            Versamento=int(input("inserisci la somma che vuoi versare"))
            conto.versamento (Versamento)
        conto.stampa_conto()
main ()





    