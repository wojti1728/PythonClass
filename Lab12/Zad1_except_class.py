''''
3 klasy wyjatkow
Nowa klasa, ma obslugiwac metodu mnozenia, dodawania i odejmowania,
akceptuje liczby calkowite,
gdy bedzie podane cos innego niz calkowita to rzuca wyjatkiem TypeError
wartosc domysla to liczba 0 (pole = 0)
jak dostatnie obiekt typu calkowitego to rzuca innym wyjatkiem
'''

'''
Wyrazenie warunkowe:
T(jezeli True) if (warunek) else F(jesli false)
SP = { '+':AA.__add__, '-':-||- __sub__, '*'
a.f(val) == f(a,val)
'''
# 3 klasy wyjatkow
class AddExc(Exception):
    pass

class SubExc(Exception):
    pass

class MulExc(Exception):
    pass

# Nasza nowa klasa

class AA:

    def __init__(self, pole=0):
        self.pole=pole

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError(other)
        else:
            if other > 0:
                raise AddExc(other)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError(other)
        else:
            if other>0:
                raise SubExc(other)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError(other)
        else:
            if other>0:
                raise MulExc(other)

#I do an object with default value 1
aa1 = AA(1)

try:
    aa1 -= 5
except Exception as e:
    print(f'Wyjatek: {type(e).__name__}, other = {e.args[0]}')

#wyrazenie warunkow: T if C else F

SP = {'+':AA.__add__, '-':AA.__sub__, '*':AA.__mul__}

def fun(a, op, val):
    f=SP[op] #wywolujemy jedna z metod na obiekcie AA które mamy sprecyzowane w SP:
    return f(a, val)

def operacja(a, op, val):
    try:
        fun(a, op, val)
    except TypeError:
        raise
    except AddExc as P:
        a.pole += 1
        val -= 1
        operacja(a, op, val)
    except SubExc as P:
        a.pole -= 1
        val -= 1
        operacja(a, op, val)

# def operacja_2(a, op, val):
#     for i in range(val)

try:
    print(aa1.pole)
    operacja(aa1,'+',8)
    print(aa1.pole)
    operacja(aa1,'-',23)
    print(aa1.pole)
except Exception as e:
    print(f'Wyjatek: {type(e).__name__}, other = {e.args[0]}')

'''
W ramach zadania poczytac o wyjatkach i zamienic to na pętle
'''

