


while True:
    a=input("Input number: ")
    is_even="even" if int(a)%2 == 0 else "odd"
    print(a,"is",is_even)

while i<10:
    print(i)
    i+=1
    
for i in range(1,11,2):
    print(i)

for letter in "some string":
   print(letter)
    
'''
my_list.append(another_list)
my_list.extend(another_list)

usuwanie po indeksie:
del my_list[0]

usuwanie po wartosci:
my_list.remove(2)

IMPORTY:

--- w importach nie pisze się rozszerzenia .py
import math  # built-in module

import utils  # our file utils.py, without the .py

1 sposób: import x, x.fun()
2 sposób: from x import fun, fun()

KROTKI:
a, b = 1, 2  # a is 1, b is 2
a, b = b, a  # now b has previous value of a - 1, and a is 2

DICTIONARIES:
dictionary = {"a": 1, "b": 2, "d": 4, "c": 3}
print(dictionary["c"])  # 3

Iterowanie po słwnikach:
for key in dictionary.keys():  # iterate through keys
for val in dictionary.values():  # iterate through values
for key, val in dictionary.items():  # iterate through key-value pairs

ZBIORY:

my_set = {1, 2, 3}
my_set.add(4)  # {1, 2, 3, 4}

Główne zastaosownanie:
if 3 in my_set:
    print("3 is in my_set")

FUNKCJE:

def count_words(string, word_to_search):
    words = string.split()  # splits string into words
    counter = 0
    for word in words:
        if word == word_to_search:
            counter += 1
    return len(words), counter
'''






