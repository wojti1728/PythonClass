### dekorowanie funkcji :
### mamy dane x,y a funkcja oczekuje danych w kolejnosci y,x
###
###funkcja f przyjmuje parametry lo,la i zwraca lo,la
### funkcja TH to jakas funkcja cos robiaca, np wykonujaca dodawanie

### przyklad schematyczny

##def R (f) :
##    def _i_ (x,y) :
##        lo,la = TH(x,y)
##        w = f(lo,la)
##        return TH**(-1)(*w)
##    return _i_

def dodaawanie(*a):
    return sum(a)

def dekor( f ):
    def _i_( *z ):
        par = [ int(n) for n in z ]
        w = dodaawanie(*par)
        return w
    return _i_

# Kacpra przyklad:

import time

def count_time(func):
    def temp(x):
        start = time.time()
        func()
        stop = time.time()
        print(f'Czas dla liczby {x} wynosi: {start-stop}')
        return start-stop
    return temp

@count_time
def timex(long):
    sum([i**3 for i in range(long)])


#timex(1000) # ?????????????????? dlaczgo to nie dziala na windowsie???

def zamiana (fun):
    def na_dziesietny(*args):
        return fun([int(x, base=4) for x in args])
    return na_dziesietny

# nauka -  dekoratory z @
a = '123' # 27
b = '123' # 27
c = '012' # 6
d = '333' # 63

@zamiana
def function(*args): # dekorator przyjmuje funkcje min/max i zamienia w nim 4 -> 10 system i wykonuje operacje
    return min(*args) * max(*args)

print(function(a, b, c))


