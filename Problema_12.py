#“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. 
#Rupând petalele unei margarete cu x petale, el (ea) mă iubeşte …. 
#Exemplu: Date de intrare: x=10 Date de ieşire: … de loc.
x=int(input("Dati numarul de petale:"))
if (x%5==1):
    print("un pic")
if (x%5==2):
    print("mult")
if (x%5==3):
    print("cu pasiune")
if (x%5==4):
    print("la nebunie")
if (x%5==0):
    print("deloc")