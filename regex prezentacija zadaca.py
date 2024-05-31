"""
Potrebno napisati regex koji vraca podudaranje
ukoliko se unese string koji počinje kao prvo slovo vašeg imena,
a završava kao prvo slovo
prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
"""

import re

# Definirajte ime i prezime
ime = "Ivan"
prezime = "Filipovic"

# Napravite regex izraz s vašim imenom i prezimenom
regex_izraz = f"^{ime[0]}.+[0-5]\\s{prezime[0]}$"

# Primjer ulaznih nizova koji bi se trebali podudarati s regexom
ulazni_nizovi = [
    "Iv4 F",
    "Ivan Filipovic",
    "I4 Filipovic",
    "Iva 1 F"
]

# Provjerite podudaranje za svaki ulazni niz
for ulaz in ulazni_nizovi:
    if re.match(regex_izraz, ulaz):
        print(f"Podudaranje pronađeno za ulazni niz: {ulaz}")
    else:
        print(f"Podudaranje nije pronađeno za ulazni niz: {ulaz}")
