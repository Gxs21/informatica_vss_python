from ContoBancario import ContoBancario
def main():
    
    nominativo=input("Nominativo: ")
    print("benvenut*",str(nominativo), "nel tuo conto corrente! vorresti prelevare una quota (1) o versare una quota (2)?")
    saldo=int(input("inserire il saldo iniziale: "))
scelta=int(input())
if (scelta==1):
    soldi=int(input("soldi da prelevare: "))
    ContoBancario.prelievo (soldi)
if (scetla==2):
        ContoBancario.versamento (soldi)

ContoBancario.
main()

