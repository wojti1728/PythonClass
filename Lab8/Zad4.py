
'''
range(10)
[*range(10)]

[*range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
{*range(10)}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
(*range(10))
SyntaxError: cannot use starred expression here
tuple(*range(10))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tuple(*range(10))
TypeError: tuple expected at most 1 argument, got 10
tuple([*range(10)])
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
type(tuple([*range(10)])_
     )
SyntaxError: invalid syntax. Perhaps you forgot a comma?
KeyboardInterrupt
type(tuple([*range(10)]))
<class 'tuple'>

enumerate(range(10))

<enumerate object at 0x00000217EE59E840>
{*enumerate('ANCD')}
{(2, 'C'), (1, 'N'), (3, 'D'), (0, 'A')}
'''

###################
'''
Napisac funkcje:
seq - pierwszy argument
sep = '->'
end = \n\t
te dwa wyzej tylko przez podstawienie
wyswietla elementy seq
np:
seq[0] sep seq[1]
przekazumeny ten słownik

'''

def CF(seq, sep = '->', end = '\n\t', **kwds):
    for e in zip(seq[1:], seq[:-1]):
        print(*e, sep=sep, end=end, **kwds) # dzięki *e rozpakowulemy krotke jako dwa parametry
        #print(*e, sep=sep, end=end, **kwds) # dzięki *e rozpakowulemy kratke jako dwa parametry
        # **kwds -> aby wszystkie dodatkowe argumenty byly wykorzystane prze print (chyba ze napiszemy glupoty to wywali blad)

s = 'ABCDEFG'
CF(s)

'''
ZADANIE:
poprawic wyszukiwanie liczb pierwszych poprzez ich zapisywanie 
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