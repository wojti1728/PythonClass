#PROGRAMOWANIE OBIEKTOWE:!

'''
OBIEKT:
-POSIADA TYPY
-POSIDA ATRYBUTY
-JEST UNIKALNY

Co musimy zrobic aby miec obiket:
W C++:
- stworzyc klase( aby byt typ)
- strzworzyc instruktor i destruktor
- pola (maja typ i identyfikator)
- to co mamy w klasie jest opisem jak ma wygladac kazda instancja
- pola ktore nie laduja w obiekcie (inczej pola statyczne!)
- metody sa atrybutami klasy
- co do pola statycznego:
- sa jeszcze metody styatyczne
- def klasy opisuje jak maja wygladac instancje

W Pythonie:
- klasa obiektem
- typem obiektu jest klasa
- metaklasa tworzy klase, klase tworzy obiekt
- aby utworzyc obiekt mozemy uzyc literaly lub konstruktora
-

'''
G = 101

class N:
    print(G)
    x = 5*chr(G)
    print(x)

n = N()
print(n.x)
print(dir(N))

n.x = 10
N.x = 10

print(n.x)
#dir(n) -> sprawdzanie atrubutow w idle

'''
Jak zbudowac atrybuty instancji?:
'''
n.y = 10
print(n.y)
del n.x
print(n.x)
N.z = 'A'
print(dir(N))
print(dir(n))

'''
class Q:
    pole = 'A'
    def f(a, b):
        print(a, b)

        
o = Q
o = Q()
dir(o)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'f', 'pole']
Q.pole
'A'
Q.F
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Q.F
AttributeError: type object 'Q' has no attribute 'F'. Did you mean: 'f'?
Q.f
<function Q.f at 0x000001F07C2079A0>
type(Q.f)
<class 'function'>
type(o.pole)
<class 'str'>
type(Q.f)
<class 'function'>
type(o.pole)
<class 'str'>
type(o.f)
<class 'method'>
O.f(10, 20)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    O.f(10, 20)
NameError: name 'O' is not defined. Did you mean: 'o'?
Q.f(10, 20)
10 20
o.f(10, 20)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    o.f(10, 20)
TypeError: Q.f() takes 2 positional arguments but 3 were given
'''

'''
Przy uruchomieniu czegos takiego:
class N:
    ...
    ...
to wtedy uruchamia sie dla nas niewidocznie metaklasa (type)
jeśli nie mamy: __init__
'''