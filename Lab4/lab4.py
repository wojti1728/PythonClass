print('Hello World')

'''
dane='SDF^r$45##@SDFsfdfd'
dane='SDF^r$45##@SDFsfdfdśę'
dane.encode
<built-in method encode of str object at 0x000001684A016EB0>
dane.encode('utf-8')
b'SDF^r$45##@SDFsfdfd\xc5\x9b\xc4\x99'
dane.encode()
b'SDF^r$45##@SDFsfdfd\xc5\x9b\xc4\x99'
C=dane.encode()
a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a
NameError: name 'a' is not defined
'a'
'a'
'a'.encode()
b'a'
'B'.encode()
b'B'
Traceback (most recent call last):
    'B'.encode()
KeyboardInterrupt
'#'.encode()
b'#'
type('#'.encode())
<class 'bytes'>
dir('#'.encode())
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

'#'.encode().upper()
b'#'
temp='#'.encode()
temp[0]='1'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    temp[0]='1'
TypeError: 'bytes' object does not support item assignment
temp[0]
35
temp[1]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    temp[1]
IndexError: index out of range
'''
l=list(range(99,109))
bytes(l)
# dodatkpwy typ danych
# bytearray
'''
bytearray(list(range(240,256))

jest mutowalny ale tylko 0-256 bajtów !!!

unicode jest wielobajtowy a CP1240 jest jednobajtowy !

C.decode('CP1250')
             
'SDF^r$45##@SDFsfdfdĹ›Ä™'
len(C.decode('CP1250'))
             
23
len(C.decode())
             
21

dane.encode('CP1250').decode('Latin2')
             
'SDF^r$45##@SDFsfdfd\x9cę'
len(dane.encode('CP1250').decode('Latin2'))
             

'''

#######################################################

'''
SŁOWNIKI !!!

Lista nie moze być kluczem !!
Kluczami mogą być typy tylko niemodyfikywalne !!!

L=dict()
             
L[1]='jeden'
             
L
             
{1: 'jeden'}
L['dwa']=[0,1]
             
L
             
{1: 'jeden', 'dwa': [0, 1]}
L[L['dwa']]=(0,)

L[(0,1,2)]=b'trzy'
             
L
             
{1: 'jeden', 'dwa': [0, 1], (0, 1, 2): b'trzy'}

L[L['dwa']]=(0,)
             
L
             
{1: 'jeden', 'dwa': (0, 1), (0, 1, 2): b'trzy', (0, 1): (0,)}

L.__contains__('jeden') -> sprawdza czy zawiera sie taki klucz!
             
False
'''


''''
Przypomniec sobie awk
poczytac o slownikach i ich metodach
i bedziemy zbiory robic
itp
'''
