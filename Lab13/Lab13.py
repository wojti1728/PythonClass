'''
Kazdy kontener


'''

'''
zad1:
zaimplementowac kolekcje par, moga byc różne pary(listy i krotki)
-najpierw obiekt jest pusty
- inaczej init jest pusty
-pozniej mamy operacje dodac (jako parametr przyjemuje obiekt i podejmuje decyzje czy mozna dodac)
-jesli nie jest krotka ani lista to rzuca wyjatkiem (typeerrror)
-jeszcze sprawdza czy jest to para bo wtedy wyrzuca valueerror
-__str__ -> ma wypisywac kolumne, poszczególne elementy w nowych liniach od tabulacji
-
'''
'''
isinstance()- krotka i lista powinny
'''
class Pairs:
    '''Colections of pairs'''
    def __init__(self):
        self.list1 = []

    def __str__(self):
        '''Print method'''
        str1 ='\t'
        str1 = '\n\t'.join(str(val) for val in self.list1)
        return str1

    def __iadd__(self, other):
        '''Add's method'''
        if( not isinstance(other, tuple) and not isinstance(other, list)):
            raise TypeError
        if( not len(other)==2 ):
            raise ValueError
        self.list1.append(other)
        return self

    def __len__(self):
        return len(self.list1)**2

    def __bool__(self):
        return (len([i for i in self.list1 if isinstance(i, list) ]) == len([i for i in self.list1 if isinstance(i, tuple)]))

p1 = Pairs()
p1.__iadd__((2,3))
p1 += (4,5)
p1 += [7,7]
p1 += [7,8]
p1 += [5,9]
p1 += (4,3)

print(p1)
q=Pairs()
print( q and True )
q += [3,4]
print( q and True)
print(p1.__len__())

print(p1.__bool__())

