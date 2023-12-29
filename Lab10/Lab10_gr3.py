'''
Podstawy do stosowania programowania funkcjynego muszą byc trkatowane jako zwykle obiekty
'''

#Definowianie funkcji w funkcji

def mul(z):
    def _in_(n):
        return z*n*1j
    print(_in_(z))

print(mul(100))

x = mul(7)

'''
funkcja wewnterzna pamieta otoczenie z momentu dopelnienia
'''

#DOMYKANIE FUNKCJI( closure )
'''
##>>> S = 10
##>>> def m2(n) :
##      return S*n
##
##>>> m2(10)
##100
##>>> S= 'abc'     #modyfikujemy S i uruchamami jeszcze raz
##>>> m2(4)
##'abcabcabcabc'
##
#### ^ tu nie mamy closure, mamy tutaj dostep do zmiennej lokalnej
##
####czasem potrzebujemy funkcji ktora modyfikuje otoczenie:
##
##
##>>> def m3(n):
##      w = S*n
##      S=n
##      return w
##
##>>> print(map(m3(range(5))))
##Traceback (most recent call last):
##  File "<pyshell#46>", line 1, in <module>
##    print(map(m3(range(5))))
##  File "<pyshell#44>", line 2, in m3
##    w = S*n
##UnboundLocalError: local variable 'S' referenced before assignment
##
#### ^ mamy blad bo uzywamy zmiennej przed jej deklarowaniem, czemu S
jest lokalne?
#### jesli w ciele funkcji pojawia sie podstawienie do symbolu, to
bedzie on lokalny
'''
# def m3(n):
#     global S
#     w = S*n
#     S = n
#     return w
#
# print(m3(10))

def mul(z):
    def _i_(n):
        global S
        S *= n
        return _i_
S = 10
mul(7)
print('S po modyfikacji: ', S)

def m2(z):
    Q = 10
    def _i_(n):
        #global Q
        #Q *= -1j
        return z*n*Q
    return _i_
S = 4
x = m2(8)
print('x(8):',  x(10))
# Q jest lokalne wzgledem m2, mozna BY bylo korzystac gdyby nie bylo podstawienia Q


# mamy nonlocal Q :

def m2(z):
    Q = 10
    def _i_(n):
        nonlocal Q
        Q *= -1j
        return z*n*Q
    return _i_
Q=10
m2(10)
print('Q=', Q)

def mul2(z):
    def _in_(n):
        global S # bez tego nie zadziala
        S *= -1j
        return z*n*S
    return _in_
S = 10
x = mul2(5)
print(x(5))

def mul22(z):
    q = 10
    def _in_(n):
        global q # bez tego nie zadziala, w sumie z tym tez nie zadziała xd
        q *= -1j
        return z*n*q
    return _in_

x = mul22(5)
#print(x(5))

#### zakresy
##
##______global_______
##|                 |
##| __nonlocal_____ |
##| |  __local_   | |
##| |  |      |   | |
##| |  |      |   | |
##| |  ________   | |
##| |             | |
##|  _____________  |
##|                 |
##___________________

#SKLADNIA IMPORTOWANIA

##
##import module
##x = module
##del module
##
##import module as x
##
### ^ sa to te same operacje
##
##
##from module import g as G
##
####
##mamy wbudowane funkcje (builtins) np print
import builtins
builtins.print
print = 10
builtins.print(print)

