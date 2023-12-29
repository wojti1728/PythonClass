#MAPOWANIE:
import math

'''
map(F, D) <-> [F(d) for d in D]
'''
d=map(chr, range(87, 114))
print(*d)

def pow3(x):
    return x**3

print(*map(pow3, range(10)))

G = lambda x : x**3.5
print(*map(G, range(10)))

#Przyklad z kołem:
P = lambda p : math.sqrt(p[0]**2+p[1]**2)
print(*map(P,zip(range(10), range(5,15))))
P2 = lambda x, y: math.sqrt(x**2+y**2)
print(*map(P2,range(10), range(5,15))) #Tutaj musi byc bez zipa !!

#Funkcja filtr:
'''
filter(p,D) <-> [
'''

#Zad 1:
'''
Nalzey wczystac tekst, ten tekst nalezy podzielic na slowa, i odfiltrowac 
te słowa ktore posiadaja min jedna duza liter!
'''
#test = input('Prosze wpisac tekst:')
test = ''
test = test.split()
new_words = []
p = lambda x: not x.islower()


#print(p(test))

print(*filter(p, test))

#ZAD 2:
'''
Ze zbioru od 0 do 600 wybrac te elementu ktorych reszta 
z dzielenie przez 5 jest nie mniejsza niz 3,
wyniki podniesc do potegi 3 i odfiltrowac z nich te 
których reprezentacja tekstowa jest parzystej dlugosci.
'''
numbers = list(range(0,600))

p1 = lambda p: p%5 >= 3
p2 = lambda p: len(str(p**3))%2 == 0
p3 = lambda p: p**3

print(*map(p3, list(filter(p2, filter(p1, numbers)))))

##############################

# REDUCE()
import functools

val = functools.reduce(int.__mul__, [*range(1,10)])
print('Val:', val)

##############################

#Obliczenia leniwe:

#################
def aim(x, y, r):
    return 0
'''
def urring(f, param):
    def inner(*args):
        return f(*args, param)
'''

