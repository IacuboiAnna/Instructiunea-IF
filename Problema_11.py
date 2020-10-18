#Se dau trei numere. Să se afişeze aceste numere unul sub altul, 
#afişând în dreptul fiecăruia unul dintre cuvintele PAR sau IMPAR. 
#Exemplu : Date de intrare : 45 3 24 Date de ieşire : 45 impar 3 impar 24 par.
a=int(input("dati nr.1:"))
b=int(input("dati nr.2:"))
c=int(input("dati nr.3:"))
if (a%2==0):
    print(a, "par")
if (a%2!=0):
    print(a, "impar")
if (b%2==0):
    print(b, "par")
if (b%2!=0):
    print(b, "impar")
if (c%2==0):
    print(c, "par")
if (c%2!=0):
    print(c, "impar")