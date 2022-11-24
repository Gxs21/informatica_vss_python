'''scrivere una funzione che usando una funzione che stabilisce se un numero è primo, visualizzi 
i primi 50 numeri primi '''
def primi (n):
    resto=0
    contatore=0
    contatore1=0
    resto1=0
    for i in range (2,n):
        resto=n%i
        if resto==0:
            contatore+=1
    if contatore==0:
        print("il nmumero " + str(n) + " è primo") 
    for j in range (1, 51):
        contatore1=0
        resto1=0
        for z in range (2,j-1):
            resto1=j%z
            if resto1==0:
                contatore1+=1
        if contatore1==0:
            print(str(j))

#main
n=0
while n<=0:
    n=int(input("inserire un numero: "))
    
print(primi (n))n
rans ''