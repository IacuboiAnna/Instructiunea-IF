#Se consideră trei numere întregi. Dacă toate sunt pozitive, 
#să se afişeze numărul mai mare dintre al doilea şi al treilea număr, 
#în caz contrar să se calculeze suma primelor două numere. 
#Exemple: Date de intrare 45 23 100 date de ieşire 100 ; Date de intrare 34 -25 10 Date de ieşire 9.
a=int(input("Dati primul numar:"))
b=int(input("Dati al doilea numar:"))
c=int(input("Dati al treilea numar:"))
if ((a>0) and (b>0) and (c>0)):
    if (b>c):
        print(b)
    if (c>b):
        print(c)
    if (b==c):
        print(b)
if ((a<0) or (b<0) or (c<0)):
    print(a+b)