
'''
Używając geta, appenda itp.. oraz metoda (setdefault)
D.setdefault(klucz, wartosc) -> podobne do geta
jeżeli klucz jest w słowniku, to zwraca D[klucz]
jezlili nie ma klucza w slowniku to D[klucz]=wartosc

klucz not in D:
    D[klucz] = wartosc
D[klucz]

'''


tekst = input('Podaj teskt skladajacy sie z wielu słów:')
#tekst = "Ala ma duzego psa a na jej domie ma ala ade z duzem"
tekst = tekst.lower()
words = tekst.split()
groups = {}
groups2 = {}
groups3 = {}
for word in words:
    # metoda pierwsza
    if not word[0] in groups:
        groups[word[0]] = []
        groups[word[0]].append(word)
    else:
        groups[word[0]].append(word)

    # druga metoda
    groups2[word[0]] = groups2.get(word[0], [])
    groups2[word[0]].append(word)

    # trzecia metoda
    groups3[word[0]] = groups3.setdefault(word[0], [])
    groups3[word[0]].append(word)

print(groups)
print(groups2)
print(groups3)