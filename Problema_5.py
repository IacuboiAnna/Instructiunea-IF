#Cunoscând data curentă exprimată prin trei numere întregi 
#reprezentând anul, luna, ziua precum şi data naşterii unei persoane, exprimată la fel, 
#să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. 
#Exemplu : Date de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani.
zn=int(input("Dati ziua nasterii:"))
ln=int(input("Dati luna nasterii:"))
an=int(input("Dati anul nasterii:"))
zc=int(input("Dati ziua curenta:"))
lc=int(input("Dati luna curenta:"))
ac=int(input("Dati anul curent:"))
if (lc>ln):
    print(ac-an, "ani")
if ((lc==ln) and (zc>=zn)):
    print(ac-an, "ani")
if ((lc==ln) and (zc<zn)):
    print((ac-an)-1, "ani")
if (lc<ln):
    print((ac-an)-1, "ani")
 