#La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare 
#albă, roşie, albastră şi neagră, în această secvenţă. 
#Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? 
#Exemplu : date de intrare : x=38 date de ieşire : rosie.
x=int(input("Dati locul lui Ionel:"))
if (x<=100):
    if (x%4==1):
        print("alba")
    if (x%4==2):
        print("rosie") 
    if (x%4==3):
        print("albastra")
    if (x%4==0):
        print("neagra")
if (x>100):
    print("Ionel nu a nimerit in prima suta de concurenti")