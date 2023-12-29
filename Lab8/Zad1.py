'''
Zanotowac kiedy funkcja byla rozpoczeta
modul time, funkcja time

Napisac funkcje, wyswietlic duzo tekstu, jeden argument to lista
do ktorej bedziemy zapisywac  czas trwania funkcji
'''

import time

def f1(tmm):
    t1 = time.time()
    for i in range(100000):
        print(i, end=' ')
    t2 = time.time()
    tmm.append(t2-t1)

tmm = []

for i in range(10):
    f1(tmm)

print(tmm)

####################

