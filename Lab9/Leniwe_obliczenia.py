#Leniwe obliczcenia

'''
#Generator:
G = (x**5 for x in range(10))
for x in G:
print(x)
'''

G = (x**5 for x in range(100))
for x in G:
    print(x)

*G, # bedzie to zwykla pusta krotka bo petla for wyciagla wszystko z G
print(*G)
G = (x**5 for x in range(100))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

for x in G:
    if x**2 > 5:
        break
    print(x)

print(*G) # sprawdzamy co zostało
print(*G) # sprawdzamy co zostało
print(*G) # sprawdzamy co zostało
'''
G = (x**5 for x in range(2))
        
next(G)

0
next(G)
        
1
next(G)
        
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    next(G)
StopIteration
'''
# funkcja generatorowa
def F(x):
    while x**3 < 10**4:
        yield x
        x += 1
g = F(15)
print(next(g))
print(next(g))

L = list(range(10000))
g = iter(L) # dostajemy iterator (mozemy robic podobne rzeczy jak z generatorami)
print(g)
# for x in L: # python zamienie to na for x in iter(L):
#     if P(x): break
#     print(x)
