'''
Zad2:
Mamy zadany łańcuch liter oraz liczbe n,
mamy w tym łańcuchu znalezc wszsytekie podlancuchy dlugisci n
ktore sa zbalansowane (czyli znaczy ze wszsytkie
litery jest tyle co innych)
- moga byc wycinki
'''

tekst = "Alal  ma duzego psa a na jej domie ma ala ade z duzem"
tekst = tekst.lower()
n=6 #nasza szerokosc szukanego podlancucha
zbior = set()

for litera in tekst:
    zbior.add(litera)

results = []
for i in range(0, len(tekst)-n):
    podlan = tekst[i:i+n]
    groups = {}
    for lit in podlan:
        groups[lit] = groups.get(lit, 0) + 1
        #print(groups)
    zbior2 = set()
    for val in groups.values():
        zbior2.add(val)
    #print(zbior2)
    if len(zbior2) == 1:
        results.append(podlan)
print(f"Results1: {results}")


''''
def counter(cn, add, sub=None):
- cn -> wkladamy slownik ktory byc moze jest juz wyoelniony
- add -> (lancuch znakowy) sa to znaki ktore ktortnosci juz znalazly sie w sloniku
- sub -> podobnie tylko odejmujemy
- funkcja zwraca argument cn!

'''

def counter(cn, add, sub=None):
    if cn is None:
        cn = {}
    if add is not None:
        for lit in add:
            cn[lit]=cn.get(lit, 0) + 1
    if sub is not None:
        for lit in sub:
            cn[lit]=cn.get(lit, 0) - 1
    return cn

tekst = "Alal  ma duzego psa a na jej domie ma ala ade z duzem"
tekst = tekst.lower()
litery2 = {}
for litera in tekst:
    # metoda druga
    litery2[litera] = litery2.get(litera, 0) + 1

print(litery2)

print(counter(litery2,'s','aaasasd'))

'''
Zad2_V2:
Mamy zadany łańcuch liter oraz liczbe n,
mamy w tym łańcuchu znalezc wszsytekie podlancuchy dlugisci n
ktore sa zbalansowane (czyli znaczy ze wszsytkie
litery jest tyle co innych)
- moga byc wycinki
'''

tekst = "Alal  ma duzego psa a na jej domie ma ala ade z duzem"
tekst = tekst.lower()
n=4

def balanced(lancuch, n):
    groups = {}
    res = []
    podlan = lancuch[0:n]
    groups = counter(groups, podlan)
    for i in range(n, len(lancuch)):
        for let in podlan:
            if len(set(groups.values())) == 1:
                res.append(i-n)



        groups.clear()
    return res

    # for i in range(n, len(lancuch)):
    #     podlan = lancuch[i - n:i]
    #     groups = counter(groups, podlan)
    #     if len(set(groups.values())) == 1:
    #         res.append(i - n)
    #
    #     groups.clear()
    # return res


print(balanced(tekst, 4))



'''
wynikiem ma byc funkja(lancuch znakoy, n) i zwraca sekwencje

metoda discard()
'''