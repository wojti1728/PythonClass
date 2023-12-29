
'''
Implemmentacja kontenera materialow sypkich:
- objetosc
- metody: dosyp, odsyp, kazda z tych metod dostaje parametr ile
- nie przejmujemy sie pojemnocia gdy np bedzie sie wysypywac
- tak samo jak wysypujemy
- float
'''

class Box:
    def __init__(self, name: str = 'Baska', volume: float = 0.0, max_volume: float = 30.0):
        self.name = name
        self.volume = volume
        self.max_volume = max_volume

    '''How to use the special methods in Python'''
    def __str__(self):
        return f'{self.name} ma objetosc: {self.volume}'
    #def __repr__(self):
     #   return repr

    def __eq__(self, other):
        #if( isinstance())
        return (self.volume == other.volume and self.max_volume == other.max_volume)

    def __add__(self, other):
        if isinstance(other, Box):
            return Box(self.name, self.volume + other, self.max_volume)
        else:
            return NotImplemented

    def __radd__(self, other):
        print('haha')
        if not isinstance(other, Box):
            return Box(self.name, other+self.volume, self.max_volume)

    # def __iadd__(self, other):
    #     try:
    #         self.volume += other
    #     except ValueError:
    #         print("Oops! That was no valid number. Try again>>>")


    # def __bool__(self):
    #     return self != 0

    def len(self):
        return int(self.volume/10)

    def add(self, value):
        self.volume += value
        if( self.volume > self.max_volume):
            self.volume = self.max_volume

    def sub(self, value):
        self.volume -= value
        if(self.volume < 0):
            self.volume = 0

K1 = Box('Janusz', 10.0, 25.0)
K11 = Box('Janusz', 10.0, 25.0)
print(f'{K1.name} ma objetosc: {K1.volume}')
K1.sub(30.35)
K1.add(5.5)
print(f'{K1.name} ma objetosc 3: {K1.volume}')

K1.add(50.5)
print(f'{K1.name} ma objetosc 4: {K1.volume}')

K3 = Box()
print(K1)
print(K3)

K4 = K1.__repr__()
print(K4)


print(K1 is K11)
z = ['a', 'b']
print(K1 == K11)
print(isinstance(z, Box))

############################
#### FUNKCJE SPECJALNE #####
K5=Box('T500', 5, 20)
print(K5.len())

K6=Box('T600', 15, 20)
print(K6.len())

#Kacze typowanie:
print(bool(K5))
print(bool(K6))

###########################
print(K5)
print(K6)
#print('K11=', K5+K6)

#print(K5+3)
print('3+K5=', 3+K5)

'''
ZADANIE:
- wyjątki (poczytać)
- 

'''