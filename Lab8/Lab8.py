

def f(el, seq=[]):
    seq.append(el)
    seq.insert(0, el)
    return seq


print(f(3))

def f(el, seq=None):
    seq.append(el)
    seq.insert(0, el)
    return seq

print(f(4, [5]))

print(type(f))

###################################

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

####################################
