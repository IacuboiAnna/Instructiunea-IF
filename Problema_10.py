#La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. 
#Cele care nu pot fi împărţite vor fi primite de curcanul Clapon. 
#Să se spună cine a primit mai multe boabe şi cu cât. 
#În caz de egalitate, se va afişa numărul de boabe primite şi cuvântul "egalitate". 
#Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea numărul de boabe de porumb. 
#Exemplu: Date de intrare 100 4050 Date de ieşire: Curcanul mai mult cu 10 boabe.
g=int(input("Dati numarul de gaini:"))
b=int(input("Dati numarul de boabe:"))
x=b//g #Numarul de boabe primite de fiecare gaina
y=b%g  #Numarul de boabe primite de curcan
if (y>x):
    print("curcanul a primit mai mult cu ", y-x, "boabe")
if (x>y):
    print("o gaina a primit mai mult cu", x-y, "boabe")
if (x==y):
    print("egalitate:", x, "boabe a primit fiecare")