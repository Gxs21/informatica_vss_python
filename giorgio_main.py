from giorgio_classe import ContoBancario
def main():
    n_conto=int(input ("inserire il numero del conto: "))
    nom=input ("inserire il suo nominativo: ")
    sal=int(input("iserisci il saldo attuale: "))
    conto = ContoBancario (n_conto, nom, sal, 0)
    while True:
        n=str(input("per prelevare inserisci:  prel , per versare vers: "))
        if n=="prel":
            Prel=int(input("inserisci la somma he vuoi prelevare: "))
            if Prel<conto.saldo:
                conto.prelievo (Prel)
        if n=="vers":
            Vers=int(input("inserisci la somma che vuoi versare: "))
            conto.versamento (Vers)
        conto.visualizza()
main ()