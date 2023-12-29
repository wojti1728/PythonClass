import site


def prez(klasa, metoda, instancja):
    pre = f'{metoda.__qualname__}'
    #pre = f'{klasa.__name__}, {metoda.__name__}'
    post = f'intancja typu {type(instancja).__name__}'
    return f'{pre}, {post}'



class A:
    '''Empty cllass'''
    def f0(self):
        print(prez(A, A.f0, self))

    def f2(self):
        print(prez(A, A.f2, self))
        print('wywolanie f0', end='\n\t')
        self.f0()

class B(A):
    def f1(self):
        print(prez(B, B.f1, self))


a1 = A()

print(a1.f0())

lf=['f0', 'f1', f'2']
n=lf[1]
print(getattr(B, n))

############################################
'''
zdefiniowac funkcje ktora przyjmuje jako pierwszy argument funkcje 
a reszste dowalna ilosc argumentow(obiektow)
- w petli wywoluje tę funkcje dla kolejnych argumentów
'''
a=A()
b=B()
# zmieniamy istniejaca klase w locie i sprawdzamy co sie tu pojawi
B.f0 = lambda self: print('.... zupelnie nowa funkcja')
'''
Powyzej nadpisujemy metode f0 ww klasie B()
- w pythonie wszsytkie metody sa efektywnie virtualne
'''

def test(fun, *args):
    for i in args:
        try:
            getattr(i, fun)()
        except AttributeError:
            print(f'Atribiute Error dla: {i}')
print('###########')
test('f1', a, b)
print('###########')
test('f0', a, b)
print('############')
test('f2', a, b)

############################
# Nowy przykład:

class X:
    def __init__(self, p):
        self.polex = p

class Y(X):
    def __init__(self, p):
        #self.__init__(p)
        #X.__init__(self, p) # to sugeruje prfesor !!!
        super.__init__(self, p) # wszystko to zamienne
        self.polex = p/2


