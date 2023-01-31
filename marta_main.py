from conto_marta import ContoBancario
def main():
    numeroConto= int(input("inseire il voostro numero di conto: "))
    nominativo=input("Nominativo: ")
    print("benvenut*",nominativo, "nel tuo conto corrente! vorresti prelevare una quota (1) o versare una quota (2)?")
    scelta=int(input())
    saldo=int(input("inserire il saldo iniziale: "))
    
    contoBanc=ContoBancario(numeroConto, nominativo, saldo, 0 )
    if (scelta==1):
        soldi=int(input("soldi da prelevare: "))
        contoBanc.prelievo (soldi)
    if (scelta==2):
        soldi=int(input("soldi da prelevare: "))
        contoBanc.versamento (soldi)

    contoBanc.stampa ()
main()

