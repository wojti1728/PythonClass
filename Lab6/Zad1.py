import math
import random
'''
Bierzemy jakas sekwencje, np liste slów, dzielimy sekwencje na pary,
(pierwsza para, druga paraa), zapuszcamy funkcje na tej sekwencje,
bierzemy te pary i robimy z nich nowe wyrazy (pierwsza litera z jednego i drugiego)

- funkcja ktora przyjmuje dwa argumenty i wypuszcza nowa sekwencje
'''

def new_word(x,y):
    z = []
    #max_len = max(len(x), len(y))
    min_len = min(len(x), len(y))
    for l in range(min_len):
            z.append(x[l])
            z.append(y[l])

    z.append(x[min_len::])
    z.append(y[min_len::])
    z = ''.join(z)
    return z

print(new_word('abcdds', 'efhdfsdfsd'))

'''
Teraz dzilenie sekwencji na pary i wywolywanie 
'''
pairs = ['1234', '54321', 'sdffsfd', 'dsf', 'fdssf','234']
nwe_pairs = []

for i in range(0,len(pairs), 2):
    pair = pairs[i:i+2]
    print(pair)
    nwe_pairs.append(pair)
    print(new_word(*pair))

'''
Strzelamy do tarczy, tarcza jest plaska, (x,y), musimy obliczyc 
jak blisko srodka ttrafilismy w srodek

def aim(x,y,r):

    return bool

return (x==10) lepsze niz ify i elsy
'''

def aim(x, y, r):
    return (x*x+y*y < r*r)

print(f"Cel {aim(3,4,3)}")

L = (1, 2, 3)
R = [0.5, 1.5, 2.5]
print(f"Zip: {zip(L,R)}")
print('Lista po zzipowaniu: ', list(zip(L,R)))

'''
Metoda seed z biblioteki random (genrator losowy)
'''

random.seed(6) #odpowiada za ziarno losowania
print(random.randint(1,5)) # randINT (czyli losuje liczby całkowite w zakresie 1-5 wlcznie)

x = [-5+10*random.random() for num in range(10)] #na potrzeby skalowania bo random.random() losuje wymierne z zakresu 0-1
y = [-5+10*random.random() for num in range(10)]
r = [-2.5+5+random.random() for num in range(10)]

print(f"R: {r}")
print(list(zip(x,y,r)))

for el in list(zip(x,y,r)): # moze byc samo zip(x,y,r) poniewaz python wie jak odczytywac ten format zip
    print(aim(*el)) # *el odpowiada za to ze bierze ta krotke aby podstawic pod odpowiednie argumenty w funkcji


