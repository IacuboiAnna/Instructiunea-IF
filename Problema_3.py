#Să se verifice dacă o literă introdusă este vocală sau consoană. Exemplu: Date de intrare  a  Date de ieşire   vocala.
l=input("dati litera:")
if ((l=='a') or (l=='A') or (l=='e') or (l=='E') or (l=='i') or (l=='I') or (l=='o') or (l=='O') or (l=='u') or (l=='U')):
    print("vocala") 
if ((l=='b') or (l=='B') or (l=='c') or (l=='C') or (l=='d') or (l=='D') or (l=='f') or (l=='F') or (l=='g') or (l=='G') or (l=='h') or (l=='H') or (l=='j') or (l=='J') or (l=='k') or (l=='K') or (l=='l') or (l=='L') or (l=='m') or (l=='M') or (l=='n') or (l=='N') or (l=='p') or (l=='P') or (l=='r') or (l=='R') or (l=='s') or (l=='S') or (l=='t') or (l=='T') or (l=='v') or (l=='V') or (l=='x') or (l=='X') or (l=='z') or (l=='Z')):
    print("consoana")
else:
    print("EROARE")
