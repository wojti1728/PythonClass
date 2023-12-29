'''Definiowanie funkcji (argumenty pozycyjne i keywords)'''

'''
Funkcja ze zmienna liczba parametrow:
def f(a, *c):
    print(a,c)
po "*c" kiedys nie 
'''

def f(a,*c,e=4):
    print(a,c,e)

f(5,3,2)

def f(a,/,*c,e=5):
    print(a,c,e)

f(5,3,2)

def f(a,/,*c,e=5,f):
    print(a,c,e,f)

f(3,34,3,f=3)

def f(a,*,i='y'):
    print(a,i)

f(5)

#Ze slownikiem:
def f(a,*c,e,**kwds):
    print(a,c,e,kwds)

f(3,23,e=4,g='assc')

###########

def p_a(a, b, **kwds):
    s = kwds.pop('end', '::\n')
    s2 = kwds.pop('g', 'sf\n')
    for x in range(a):
        print(b, s2, end=s)

p_a(3,5, s='342')

def p(x, y):
    print(x,y)

pxy = (3,4)
p(*pxy)
