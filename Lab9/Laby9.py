'''
Gdy podkładamy pod wycinek to nie tworzymy nowego obektu tylko modyfikujemy ten sam
'''

'''
Bierzemy sobie tekst
'''
T = 'ABCDefghtijklmno'
print(*T, sep='*') #*T rozpakowuje sekwejce, jakby sie wpialo pojedyncze znaki po przecinkach

D = {}
for i in range(1920,1930):
    D['sep'] = chr(i)
    print(*T, **D) #musza byc dwie gwiazdki bo D jest slownikiem

##############################################

N = open('wynik.txt', 'wt')


def CF(seq, sep = '->', end = '\n\t', **kwds):
    for e in zip(seq[1:], seq[:-1]):
        print(*e, sep=sep, end=end, **kwds) # dzięki *e rozpakowulemy krotke jako dwa parametry
        #print(*e, sep=sep, end=end, **kwds) # dzięki *e rozpakowulemy kratke jako dwa parametry
        # **kwds -> aby wszystkie dodatkowe argumenty byly wykorzystane prze print (chyba ze napiszemy glupoty to wywali blad)

s = 'ABCDEFG'
CF(s, file=N)  #parametrem file zmieniamy miejsce docelowe naszego wywołania print w funkcji CF
N.close()


'''
range(10)
range(0, 10)
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(*range(10))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(*range(10))
TypeError: list expected at most 1 argument, got 10
[*range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
{*range(10)}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

## jako generatory:

type(())
<class 'tuple'>
type((1,))
<class 'tuple'>
(*range(10),) ------------ bardzo wazny ten przecinek
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

'''
# MAP -> mapowanie !!!!!!!!!, zwraca generator

L = range(96, 106)
print(list(L))
print(list(map(chr, L))) # w sumie robi to samo co list comprehension

# FILTER, filter(p, L), tkaze zwraca generator

def parzy(x):
    return x%2 == 0
print(*filter(parzy, range(10)))

'''
def parzy(x):
    return x%2 == 0

*filter(parzy, range(10)), # bardzo wazny ten przecinek w trybie interaktywnym
(0, 2, 4, 6, 8)
# takze filter() mozna zastapic list komprehension
'''

L = [*range(1,10)]
print(L)

import functools

print(functools.reduce(int.__mul__, L)) # reduce niestety nie zamienimy na list comprehensions

###############################################

# FUNCKJE ANONIMOWE (lambda)!!!:
P = lambda x: x%2==0
print(P(10))
print(P(10), range(10))