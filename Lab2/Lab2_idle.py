print(1+3)
print(2**16)
print("Hello World")

'''
    zad 1:
    wczytuje liczbe calkowita i drukuje pomnozona przez 10
'''
a=int(input("Podaj liczbe calkowita: "))

print("Number: ",10*a)

'''
    zad 2:
    wczytuje 2 liczbe calkowita i znalezc mniejsza i wieksza z nich:
'''
#a, b=int(input("Podaj 2 liczby  calkowite: "))
a=int(input("Podaj 1 liczbe calkowita: "))
b=int(input("Podaj druga liczbe calkowita: "))
mm=min(a,b)
mx=max(a,b)
for i in range(mm,mx+1):
    print(i)
while mm<=mx:
    print(mm)
    mm+=1

