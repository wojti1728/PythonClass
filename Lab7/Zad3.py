'''
Leniwe obliczenia !!!
'''

'''
Mamy zbiór danych 

'''

'''GENERATOR'''

'''
(x*x for x in range(31) if x%3)
<generator object <genexpr> at 0x000001D6E0B9B6F0>
list((x*x for x in range(31) if x%3))
[1, 4, 16, 25, 49, 64, 100, 121, 169, 196, 256, 289, 361, 400, 484, 529, 625, 676, 784, 841]
g = (x*x for x in range(31) if x%3)
g[0]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    g[0]
TypeError: 'generator' object is not subscriptable
'''
'''
next(g)
1
next(g)
4
for x in g:
    print(x)
'''

def f(n):
    x=0
    while x<=n:
        if x%3:
            yield x*x
        x+=1

for num in f(31):
    print(num)