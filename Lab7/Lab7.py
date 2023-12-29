import copy
'''
L
L[:] - listitem
L[:] - getitem


'''

#   Zadanie 1: ############
'''

'''

L = [ e%3 for e in range(15) ]
print(L)
L2 = set()
L.sort()
print(len(L))
print(L)
for i in range(len(L)-2, -1, -1):
    print(i, end=' ')
    if (L[(i+1)] == L[i]):
        L.pop(i) # wyrzuca z listy wartosc pod indeksem 'i'

print('\n', L)

############ zad2: ############
'''Bierzemy nasz slownik z zadania z sprzed kilku zajec'''

tekst = "Ala ma duzego psa a na jej domie ma ala ade z duzem"

tekst = tekst.lower()
words = tekst.split()

groups = {}
for word in words:
    groups[word[0]] = groups.get(word[0], []) # jesli w kluczach znajduje sie word[0] to nic nie robimy ale w przeciwnym przypadku pod groups[word[0]] wstawia []
    groups[word[0]].append(word)
for i in groups.keys():
     groups[i] = list(set(groups[i]))

print(groups)

'''Wszystkie elementy we wszsytkich listach maja byc zlozone 
z duzych liter
'''

K = groups.copy()
for key, value in K.items():
    L = []
    for el in K[key]:
        L.append(el.upper())
    K[key] = L

for key, value in K.items():
    value[:] = [i.upper() for i in value]

print(K)


#############################

'''
copy.deepcopy()
'''
K1 = copy.deepcopy(groups)
for key, value in K1.items():
    value[:] = [i.upper() for i in value]

print(K1)