#Napisati rekurzivnu funkciju koja kao parametar prima string,
# a kao rezultat taj string ispisuje sa zada.

def ispis_sa_zada(a):
    if a=="":
        return
    ispis_sa_zada(a[1:])
    print(a[0], end="")

tekst="Programiranje"
ispis_sa_zada(tekst)
print()
    
