#Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. 
#Radu este pe locul x în ordinea mediilor. În ce clasa va fi repartizat (A, B, C, D sau E)?. 
#Exemplu : date de intrare : x=73 date de ieşire : C.
x=int(input("Dati locul dupa medie al lui Radu:"))
if (x<=125):
    if ((x>=1) and (x<=25)):
        print("clasa A")
    if ((x>25) and (x<=50)):
        print("clasa B")
    if ((x>50) and (x<=75)):
        print("clasa C")
    if ((x>75) and (x<=100)):
        print("clasa D")
    if ((x>100) and (x<=125)):
        print("clasa E")
if (x>125):
    print("Media lui Radu era prea mica pentru ca el sa treaca in clasa a V-a")