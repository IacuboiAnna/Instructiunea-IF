#Se introduc trei date de forma număr curent elev, punctaj. 
#Afişaţi numărul elevului cu cel mai mare punctaj. 
#Exemplu: Date de intrare  nr crt  7  punctaj 120  nr crt  3  punctaj 100 nr crt 4 punctaj 119  
#Date de ieşire  punctaj maxim are elevul cu nr crt 7.
nr1=int(input("Numarul primului elev:"))
p1=int(input("Punctajul primului elev:"))
nr2=int(input("Numarul elevului al doilea:"))
p2=int(input("Punctajul elevului al doilea:"))
nr3=int(input("Numarul elevului al treilea:"))
p3=int(input("Punctajul elevului al treilea:"))
if ((p1>p2) and (p1>p3)):
    print("Punctajul maxim are elevul cu numarul", nr1)
if ((p2>p1) and (p2>p3)):
    print("Punctajul maxim are elevul cu numarul", nr2)
if ((p3>p1) and (p3>p2)):
    print("Punctajul maxim are elevul cu numarul", nr3)
if (p1==p2):
    print("Punctajul maxim il au elevii cu numerele", nr1,nr2)
if (p2==p3):
    print("Punctajul maxim il au elevii cu numerele", nr2,nr3)
if (p1==p3):
    print("Punctajul maxim il au elevii cu numerele", nr1,nr3)