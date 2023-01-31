from classecontobancario input Contobancario
def main()
nr_conto=int(input ("inserire il numero del conto"))
nominativo=input ("inserire il suo nominativo")
saldo=int(input("iserisci il saldo attuale"))
conto=Contobancario (nr_conto,nominativo,saldo)
prosegui=p
while prosegui==1:
    n=str(input("per prelevare inserisci p , per versare v"))
    if n==p:
        Prelievo=int(input("inserisci la somma he vuoi prelevare"))
        if Prelievo<conto.getSaldo():
            conto.prelievo (saldo,Prelievo)
    if n==v:
        Versamento=int(input("inserisci la somma che vuoi versare"))
        conto.versamento (Versamento)

main ()





    