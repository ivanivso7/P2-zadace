"""
Funkciju iz prethodne zadaće (rekurzija) učitati kao funkciju modula
u novi program i pozvati je nakon traženja unosa od korisnika.
"""
from rekurzija import ispisi_unazad

string = input("Unesite string: ")

print("String unazad je: ", end="")
ispisi_unazad(string)
print()
