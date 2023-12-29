'''
Zad1:
Mamy zrobic taka liste w korej sie nie powatarza
'''

tekst = "Ala ma duzego psa a na jej domie ma ala ade z duzem"

tekst = tekst.lower()
words = tekst.split()

groups = {}

for word in words:
    groups[word[0]] = groups.get(word[0], [])
    groups[word[0]].append(word)
print(groups)
for i in groups.keys():
     groups[i] = list(set(groups[i]))

# for zm in groups.items():
#     print(zm)

print(groups)