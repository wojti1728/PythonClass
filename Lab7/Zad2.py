import math
'''
Npisac funkcje ktora sprawdza liczbe czy jest pierwsza czy nie:
'''

def ispierw(N):
    for i in range(2, int(math.sqrt(N))+1):
        if (N % i) == 0:
            return False
    return True

print(ispierw(17))


'''
for zm in seq:
...
    break (to wyskakujemy poza cala petla oraz poza elsa)
else:
'''

def lowerpierws( N ):
    P = []
    for i in range(2, N):
        for el in P:
            if (i%el == 0):
                break
        else:
            P.append(i)
    return P

print(lowerpierws(30))