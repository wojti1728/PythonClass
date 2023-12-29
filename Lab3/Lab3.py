
'''
dir -> wyswietla nam zbior operatorow (te bez podkreśleń oznaczają że możemu cos modyfikować)

'''

print(1 .__add__(1))
print((1).__add__(1))

# wczzytujemy tekst i wypisujemy znaki od konca (indeks -1 -2 -4 -7 -11 ...)
tekst=str(input("Podaj tekst:"))
i=0
skok=-1
while len(tekst)>abs(skok):
    print(tekst[skok])
    i=i+1
    skok=skok-i


''''
elementem łańcucha jest łańcuch

LISTY I KROTKI !:
(List i Tuple)

literał - stała tekstoewa która reperezentuje konkretny type
literał reprezentujacy teksu to tekst w cucdzysłowach

list-jako nazwa typu jest również konstrukltorem 

list()
list(range(5))
list(6) -> BLĄD
list('abcd')
jak sprawdzamy metody : 
dir(list) ->(te wszystkie ktore sa bez podkreslenia sa czesto uzywane)

TUPLE:
tuple() -> pusta krotka

tuple(list('abcd'))

Aby odroznic wyrazenie algebraiczne od krotki:
(1+2)*3
(1+2,)*3

listy i krotki to sekwencje!

krotka jest typem niemutowalnym a lista typem mutowalnym !!!


'''

# Zad2:
L='tekst'
L=list(L)
L=tuple(L)
L=str(L)

# komenda by przerobic tuple na lancuch tekstowy to:
T=tuple(list('tekst'))
print('#'.join(T))

# ZAD 3: Napisac skrypt, wczystac tekst, w tym teksscie na parzystych pozycjach zmieni znaki i wstawi tak o
# kodzie 4 krotnym kodu)

# funkcjie: chder

#ord(letter),chr(ord(letter))