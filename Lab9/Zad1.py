'''

Uzytkownik wprowadza lancuch tekstowy
towrzymy nowy slownik i generator ktory bedzie dostarczal slownik z kluczem 'sep' i z
kluczem 'count'

generator -> { sep: char.. , count: int}
count = randint(4, 10)
sep = randint(1600, 2800)

D -> CF( **D)
count+end(';') for in range(count)

'''
import random

def CF(seq, sep = '->', end = '\n\t', **kwds):
    for e in zip(seq[1:], seq[:-1]):
        print(*e, sep=sep, end=end, **kwds) # dzięki *e rozpakowulemy krotke jako dwa parametry
        #print(*e, sep=sep, end=end, **kwds) # dzięki *e rozpakowulemy kratke jako dwa parametry
        # **kwds -> aby wszystkie dodatkowe argumenty byly wykorzystane prze print (chyba ze napiszemy glupoty to wywali blad)

while( input('Czy nadal iterowac: ') != ''):
    T = input('Wprowadz krotki tekst:')

    def generator(T):
        for i in T:
            yield {'sep': chr(random.randint(1600, 2800)), 'count': int(random.randint(4, 10))}

    D = generator(T)

    def F(D, T):
        temp = D.pop('count')
        D['end'] = ';'
        for i in range(temp):
            CF(T, **D)
        print()

    F(next(D), T)





# napisac funkcje ktora dostanie wygenerowany slownik oraz ten tekst

'''
Funkcje, zakres widocznosci, funkcje wewnetrzne, importowanie modulow
'''
