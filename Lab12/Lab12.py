
'''
-każda metoda jest atrybutem
-domyslne dziedziczenie
- do wypisywania dwie metody (str i repr)
-str jest dziedziczona po object
-str w object nic nie robi lecz tylko wywoluje repr
O=NaszaKlasa()
    str(O)
repr(O) -> bezposrednie wywolanie repr

KOLOKWIUM:
-----------------------------------
-wszystkie metody są polimorficzne
-dommysle repr, wyswietla najczesciej nazwa i adres
-str - aby przygotowac łancuch tekstowy do reprezentacji tekstowej
-metoda eq
'''

###################################
# WYJATKI !:

class Box:
    def __init__(self, name: str = 'Baska', volume: float = 0.0, max_volume: float = 30.0):
        self.name = name
        self.volume = volume
        self.max_volume = max_volume

    '''How to use the special methods in Python'''
    def __str__(self):
        return f'{self.name} ma objetosc: {self.volume}'

    # def __repr__(self):
    #   return repr

    def __eq__(self, other):
        # if( isinstance())
        return (self.volume == other.volume and self.max_volume == other.max_volume)

    def __add__(self, other):
        if isinstance(other, Box) != False:
            return Box('df', self.volume + other, 25)
        else:
            return NotImplemented

    def __radd__(self, other):
        print(other)
        if (isinstance(other, Box) == False):
            return Box('New One', other + self.volume, 25)

    '''Exception and RAISE:'''
    def __iadd__(self, other):
        if(self.volume + other > self.max_volume):
            raise ValueError('za duzo') # rzucanie wyjątkiem (raise)
        return Box('New One', self.volume + other, 25)

    # def __bool__(self):
    #     return self != 0

    def len(self):
        return int(self.volume / 10)

    def add(self, value):
        self.volume += value
        if (self.volume > self.max_volume):
            self.volume = self.max_volume

    def sub(self, value):
        self.volume -= value
        if (self.volume < 0):
            self.volume = 0

B1=Box('T1', 12, 25)
B2=B1.__iadd__(2)
print(B2)
try:
    B1.__iadd__(23)
except ValueError as e: #mozna np expect (TypeError, SystemError):
    print(e)
    print(f"Zlapany wyjatek {type(e).__name__}")
    # e ma wiele parametrow
    # e.args[0]
except: # expect bezparametrowy musi byc na koncu
    print('A jednak blad!')
#B1.__iadd__(23)

''''
3 klasy wyjatkow
Nowa klasa, ma obslugiwac metody mnozenia dodawania,
akceptuje liczby calkowite,
gdy bedzie podana cos innego niz calkowita to rzuca wyjatkiem TypeError
wartosc domysla to liczba 0
jak dostatnie obiekt typu calkowitego to rzuca innym wyjatkiem
'''

'''
Wyrazenie warunkowe:
T(jezeli True) if (warunek) else F(jesli false)
SP = { '+':AA.__add__, '-':-||- __sub__, '*'
a.f(val) == f(a,val)
'''

# class AddExc():
#     def __init__(self):
#         self.va
#
# def operacja(ob, op, ang):
#     try:
#         #cos tu robimmy
#     except TypeError:
#         raise
#     except AddExe as P:
#         ob.pole += 1
#         ang += 1

'''
AddExc(n)
SubExc()
MatExc()
'''

'''
W ramach zadania poczytac o wyjatkach i zamienic to na pętle
'''
