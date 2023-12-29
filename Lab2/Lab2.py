
# TYPY
# w jezyku C:
# short
# int - 4 bajty = 32bity
# long int
'''

na 1 bajt = 8 bitach można uzyc 2^8 roznych wartosci
2 bajtowe = mozna wpisac wartosci 2^16
4 bajtowe = mozna woisac wartosci do 2^32

OBIEKT:
-posiada typ
-atrybubty(funkcje)
-indetyfikator (funkcja sprawdzajaca dir())
'''

print(7/2)
print(7//2)
print(4.5%1)
print(type(123.42))

'''
liczby zespolone z j jako urojona:
'''

print(1+1j)
print(type(1+1j))

'''
Łańcuch tekstowy:
char* -> wkaznik na jakies miejsce w pamieci gdzie cos wystepuje

kod ASCII ma 127 wartosci
znaki kon ca liini "\n"

UNICODE:


'''

print("alp")

string=input("Wpisz krotki łańcuch: ")
for letter in string:
    print(letter,type(letter), ord(letter),chr(ord(letter)))

chr(4000) # funkcja zamieniajaca liczbe na znak

