
'''
T[...]
__getitem()__
__setitem()__
slice(start, stop, step)
--rozpakowanie krotek
potrzebne bedzie:
zip,
slice,
rozpakowanie krotek do paramterow


'''
import random

T = [ l%3 for l in range(0,100)]
L = [ random.randint(0, int(len(T)/2)) for e in range(0, len(T)-1) ]
P = [ random.randint(int(len(T)/3), len(T)) for e in range(0, len(T)-1) ]

def f3(L, P, T):
    S32 = [T[slice(*e)] for e in zip(L, P)] # najwazniejsze to: *e, rozpakowauje krotke a w polaczeniu z slice(*e) wskazuje przedzial
    return S32

print(f3(L, P, T))

