#Să se verifice dacă o literă introdusă este vocală sau consoană. Exemplu: Date de intrare  a  Date de ieşire   vocala.
l=input("dati litera:")
if ((l=='a') or (l=='ă') or (l=='â') or (l=='e') or (l=='i') or (l=='î') or (l=='o') or (l=='u')):
    print("vocala") 
else:
    print("consoana")