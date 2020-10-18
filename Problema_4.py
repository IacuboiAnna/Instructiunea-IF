#Se introduc vârstele a 3 persoane. Afişaţi vârstele cuprinse între 18 şi 60 de ani.
#Exemplu : Date de intrare 56 34 12 Date de ieşire 56 34.
a=int(input("Dati varsta primei persoane:"))
b=int(input("Dati varsta persoanei a doua:"))
c=int(input("Dati varsta persoanei a treia:"))
if ((a>=18) and (a<=60)):
    print(a)
if ((b>=18) and (b<=60)):
    print(b)
if ((c>=18) and (c<=60)):
    print(c)
else:
    print("Nicio varsta din cele date nu se afla in intervalul 18 si 60 de ani")