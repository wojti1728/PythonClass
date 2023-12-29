
# ZAD 3: Napisac skrypt, wczystac tekst, w tym teksscie na parzystych pozycjach
# zmieni znaki i wstawi tak o kodzie 4 krotnym kodu)

# funkcjie: chder

#ord(letter),chr(ord(letter))

tekst=input("Latwe zdanie prosze:")
i=1
tekst2=list(tekst)
while (len(tekst)-i)>0:
    tekst2[i]=(chr(4*ord(tekst[i])))
    i=i+2
print(tekst2)
tekst2=''.join(tekst2)
print(tekst2)

tekst=input("Latwy wyraz prosze:")
i=1
tekst2=list(tekst)
while (len(tekst)-i)>0:
    tekst2[i]=tekst2[i]*i
    i=i+1
tekst2=''.join(tekst2)
print(tekst2)