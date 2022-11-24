"""scrivere un programma che esegua versamenti, prelievi e bonifici su un conto corrente 
e visualizzi su richiesta il numero di ognuna operazione svolta e il corrispondente importo totale"""
def versamento_funzione (conto):
    
    versamenti_tot=0
    versamento=float(input("inserisci la somma da versare sul conto"))
    while versamento<=0:
        versamento=float(input("inserisci la somma da versare sul conto"))
    conto=conto+versamento
    versamenti_tot+=versamento
    contatore_versamenti=0
    contatore_versamenti+=1
    return conto, contatore_versamenti, versamenti_tot

conto=100

print(versamento_funzione(conto))