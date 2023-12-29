#DEKORATORY:
'''
F(g, ...):
    g()
    return 42
'''
'''
@staticmethod
def mymult(...):
    pass
'''
# ZAD1:
'''
Mamy funkcje ktora uruchamia druga funkcja ktora jest jej 
argumentem, jej zadniem jest uruchomienie danej funkcji z 
zadanymi parametrami ale wczesniej podbiera czas i po tym pobiera 
czas ale w miedzy czasie zwraca wartosc
 
napisy, 
'''
import time

def G(x, y):
    for i in range(x**y):
        pass
    return x**(y*y)

def G2( G, x, y):
    start = time.time()
    temp = G(x, y)
    stop = time.time()
    return temp, stop-start

print(G2(G, 5, 8))

# Porzadny przyklad

def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def add_together(a, b):
    return a + b

print(add_together([(1,3), (3, 17), (5,5)]))

## Another example:

def meta_decorator(power):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [(fnc(val[0], val[1])) ** power for val in list_of_tuples]
        return inner
    return decorator_list


@meta_decorator(3)
def add_together(a, b):
    return a + b


print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

