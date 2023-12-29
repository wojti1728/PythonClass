''''
Wczytujemy tekst, tekst skalda sie z wielu słów,
 dzielimy go splitem, podzielić na listy aby
kazda z tych liczb skłądała się ze
słów zaczynającej się na tej samej litery

# metoda druga
    litery2[litera] = litery2.get(litera, 0) + 1
'''

# tekst = input('Podaj teskt skladajacy sie z wielu słów:')
tekst = "Ala ma duzego psa a na jej domie ma ala ade z duzem"
tekst = tekst.lower()
words = tekst.split()
groups = {}
groups2 = {}
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

print(groups)
print(groups2)
