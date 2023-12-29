'''
Zadanie 1:
c:

'''

#tekst=input("Podaj łańcuch tekstowy:")
tekst="Wczytjemy lancuch tekstowy i obliczamy ilosc poszczegowlnych liter"
litery = {}
litery2 = {}

for litera in tekst:
    # pierwsza metoda
    if( litera in litery):
        litery[litera]+=1
    else:
        litery[litera]=1
    # metoda druga
    litery2[litera] = litery2.get(litera, 0) + 1



print(sorted(litery.items(), key=lambda x: x[1]))
print(litery2)

