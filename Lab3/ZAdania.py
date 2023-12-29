'''

zad2:
na pozycjach niparzystych wkleic wartosci z pozycji sasiadujacych

'''

s=str(input("Podaj tekst:"))
L=list(s)
if( len(L)%2==0):
    L[0::2] = L[1::2]
else:
    siz=len(L)
    L[0:(siz-1):2] = L[1:(siz-1):2]
    L[len(L)-1]=L[len(L)-2]
L=''.join(L)
print(L)