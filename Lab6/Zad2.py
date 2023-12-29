'''COMPREHENSION !!!'''
import random

'''
[ x**3 for x in range(1, 10) ]
[ x**3 for x in range(1, 10) if x%3 ]
'''

'''mamy wczystac teksu, podzielic na slowa, wejscie jedna litera
'''

def the_same_letter(tekst, let):
    words = tekst.split()
    words = [word for word in words if word[0] == let]
    return words

print(the_same_letter('ala ma aleksanda ma alebo duzo ludzi mama', 'm'))

''' Losujemy liczby z zakresu 1-10, zadajemy sobie pytanie ile razy
bedzie wylosowana 5 ( n to ilosc naszych lsowan)
'''

def c5(N, s):
    random.seed(s)
    numbers = [random.randint(1,10) for num in range(1,N)]
    amount5 = numbers.count(5)
    return amount5

print(c5(5000,44))

'''Comprehension for dictionaries: 
{ x:x**3 for x in range(1, 10) if x%3 }
'''

''' Za pomoca list comprehension liste list, 
(ma byc tabliczke mnozenia)
'''
tab_mnoz = [[j*i for i in range(1,12)] for j in range(1,12)]

for line in tab_mnoz:
    print(line)



