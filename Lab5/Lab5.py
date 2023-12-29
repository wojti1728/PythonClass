
''''
ZBIORY!
set() -> zbiór pusty
S=set()

s.add(1)
s
{1}
s.add(2)
s
{1, 2}
s.add(())
s.add('aba')
s
{1, 2, (), 'aba'}
s.add([])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add([])
TypeError: unhashable type: 'list'
frozenset()
frozenset()

###################################

bytes([69,75])
b'EK'
bytes(10)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
type(bytes(10))
<class 'bytes'>

wyniki z 'b' na poczatku to literaly

###################################

slowniki:

for key, value in C.items():


#########
type(None)
<class 'NoneType'>
5 is None
False
0 is None
False
None is None
True
not 5 is None
True
not None is None
False
5 is not None
True


'''