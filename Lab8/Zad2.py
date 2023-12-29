''''
Jest lista, trzeba wygenerowC WYCINKI TEJ listy,

T = []
L = [] # len(T)-1, liczby calkowite z zakresu [0, len(T)/2]
P = [len(T)/3, len(T)]
za pomoca append() utworzyc liste S1 = [ T[L[0]:P[0]], T[L[1]:P[1]],...]
'''

import random

random.seed(0)

T = [ l%3 for l in range(0,100)]
L = [ random.randint(0, int(len(T)/2)) for e in range(0, len(T)-1) ]
P = [ random.randint(int(len(T)/3), len(T)) for e in range(0, len(T)-1) ]
S1 = []

for i in range(0,len(T)-1):
    S1.append(T[L[i]:P[i]])
print(S1)

S2 = [ T[L[i]:P[i]] for i in range(0, len(T)-1)]
print(S2)

# zip()
print(list(zip(L, P))) #laczy w krotki pierwszy z pierwszym, drugi z drugim elementem itd.
print(list(zip('ABCD', (11, 15, 17, 19)))) #combine to the time when min(len) finished

#S3 = [ list(zip(T[L[e]:P[e]]) for e in range(0, len(T)-1))]
S3 = []
for i in zip(L, P):
    S3.append(T[i[0]:i[1]])

S32 = [ T[e[0]:e[1]] for e in zip(L, P)]

print(S3)
print(S32)

