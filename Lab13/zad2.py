
class Niepuste:
    def __init__(self, obiekt1):
        self.obiekt1 = obiekt1

    def test(self):
        if( len(self.obiekt1) ):
            return self.obiekt1

class Pairs(Niepuste):
    '''Colections of pairs'''
    def __init__(self):
        super.__init__()
        self.list1 = []

    def __str__(self):
        '''Print method'''
        str1 ='\t'
        str1 = '\n\t'.join(str(val) for val in self.list1)
        return str1

    def __iadd__(self, other):
        '''Add's method'''
        if( not isinstance(other, tuple) and not isinstance(other, list)):
            raise TypeError
        if( not len(other)==2 ):
            raise ValueError
        self.list1.append(other)
        return self

    def __len__(self):
        return len(self.list1)**2

    def __bool__(self):
        return (len([i for i in self.list1 if isinstance(i, list) ]) == len([i for i in self.list1 if isinstance(i, tuple)]))



'''
ZADNIE:
- łapanie wyjatkow (wszystko, razem z final!)
- (try, expect, raise, final
- sekacje dozorowane (komenda with ...) - obsluga plikow itp (nie trzeba zamykac plików)
- 
'''

