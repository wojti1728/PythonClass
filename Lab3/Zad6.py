# zadanie

# (1+3)*4

# INDEKSOWANIE ROZSZERZONE:
S='ABCDEFGHIJ'
L=list(S)

'''
tworzenie kopie (nowego obiektu)

s[3:5]+s[7:11]
'dehij'
s[0:len(s)]
'abcdefghij'
s[None:None]
'abcdefghij'
s[:]
'abcdefghij'

L=list(s)
L[None:None:-1]
['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
L[len(L)::-1]
['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

L[2:4]=" "
L
['a', 'b', ' ', 'g', 'h', 'i', 'j']
L[2:6]=" "
L
['a', 'b', ' ', 'j']

'''

# ZADANIE!
# wczytujemy tekst, co druga znak na duza litera (uwazac na nieparzysta znak)
s=str(input("Podaj tekst:"))
L=list(s)
L[1::2]=s[1::2].upper()
L=''.join(L)
print(L)