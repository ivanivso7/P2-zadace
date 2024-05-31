"""
Zadano je natjecanje za pjesmu Eurovizije u kojem sudjeluje 37 država.
Svaka država je predstavljena s uređenim parom koji sadrži ime države,
ime izvođača i ime pjesme
 npr. ("Croatia", "Baby Lasagna", "Rim Tim Tagi Dim"),

Nasumično odabrati 26 država koje će se natjecati u finalu
i dodati ih u novu listu rječnika oblika:
{
  "drzava": "Croatia",
  "izvodjac": "Baby Lasagna",
  "pjesma": "Rim Tim Tagi Dim"
}
Nakon izbora finalista, potrebno je simulirati glasanje.
Svaka država s popisa 37 drzava moze glasati.

Nasumice se dodjeljuju se bodovi (12, 10, 8, 7, ..., 1)
nekoj od država finalista.

Drzava ne moze glasati sama za sebe.
Bodove spremati u novo svojstvo rječnika "bodovi".

Nakon glasanja ispisati pobjedničku državu - ona koja ima najvise bodova.
Za svaku državu ispisati broj bodova.
Zbrojiti i ispisati ukupan broj dodijeljenih bodova.

Proci kroz sve finaliste i pomoću regexa (dakle ne pomoću len ugrađene funkcije)
provjeriti i ispisati sve države koje u naslovu pjesme imaju vise od 10 slova.

Rezultat zapisati u datoteku u obliku

drzava,pjesma,izvodjac,bodovi
drzava2,pjesma2,izvodjac2,bodovi2

"""


import random
import re

sve_drzave = [
    ("Hrvatska", "Baby Lasagna", "Rim Tim Tagi Dim"),
    ("Švedska", "Zara Larsson", "Dance Queen"),
    ("Francuska", "Jean Dupont", "La Vie En Rose"),
    ("Njemačka", "Hans Müller", "Liebeslied"),
    ("Italija", "Giovanni Rossi", "Amore Mio"),
    ("Španjolska", "Carlos Ruiz", "Baila Conmigo"),
    ("Portugal", "Ana Silva", "Fado do Amor"),
    ("Norveška", "Ingrid Olsen", "Northern Lights"),
    ("Danska", "Lars Jensen", "Summer Night"),
    ("Finska", "Mikko Virtanen", "Winter Melody"),
    ("Island", "Bjorn Sigurdsson", "Volcano Song"),
    ("Irska", "Patrick O'Reilly", "Emerald Isle"),
    ("Ujedinjeno Kraljevstvo", "Emily Brown", "Heart of Gold"),
    ("Nizozemska", "Sven van Dijk", "Tulip Fields"),
    ("Belgija", "Marie Dupuis", "Chocolate Love"),
    ("Švicarska", "Hans Ziegler", "Mountain Song"),
    ("Austrija", "Klaus Hofer", "Vienna Waltz"),
    ("Grčka", "Nikos Papadopoulos", "Sirtaki Dance"),
    ("Cipar", "Maria Georgiou", "Island Dream"),
    ("Srbija", "Jovan Petrovic", "Balkan Beat"),
    ("Crna Gora", "Miloš Kovačević", "Adriatic Sea"),
    ("Slovenija", "Luka Novak", "Alpine Song"),
    ("Sjeverna Makedonija", "Ana Petrovska", "Skopje Nights"),
    ("Albanija", "Erik Hoxha", "Tirana Dream"),
    ("Bugarska", "Ivan Ivanov", "Rose of the Balkans"),
    ("Rumunjska", "Elena Popescu", "Carpathian Melody"),
    ("Mađarska", "Bálint Nagy", "Budapest Nights"),
    ("Poljska", "Jan Kowalski", "Polish Heart"),
    ("Češka", "Pavel Novák", "Prague Waltz"),
    ("Slovačka", "Marek Horvath", "Danube Song"),
    ("Estonija", "Katrin Tamm", "Baltic Breeze"),
    ("Latvija", "Andris Bērziņš", "Riga Nights"),
    ("Litva", "Agnė Petrauskaitė", "Vilnius Dream"),
    ("Ukrajina", "Oksana Ivanenko", "Kiev Sunrise"),
    ("Moldavija", "Ion Ceban", "Dniester Melody"),
    ("Gruzija", "Nino Kalandadze", "Caucasus Song")
]

finale_drzave = random.sample(sve_drzave, 26)

finale_list = [
    {
        "drzava": drzava,
        "izvodjac": izvodjac,
        "pjesma": pjesma,
        "bodovi": 0
    }
    for drzava, izvodjac, pjesma in finale_drzave
]

bodovi = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]

for drzava, izvodjac, pjesma in sve_drzave:
    moguci_glasaci = [entry for entry in finale_list if entry["drzava"] != drzava]
    random.shuffle(moguci_glasaci)
    
    glasovi = random.sample(moguci_glasaci, 10)
    
    for i, entry in enumerate(glasovi):
        entry["bodovi"] += bodovi[i]

pobjednik = max(finale_list, key=lambda x: x["bodovi"])

print(f"Pobjednička država je {pobjednik['drzava']} s {pobjednik['bodovi']} bodova.\n")

ukupni_bodovi = 0
for entry in finale_list:
    print(f"Država: {entry['drzava']}, Bodovi: {entry['bodovi']}")
    ukupni_bodovi += entry['bodovi']

print(f"Ukupan broj dodijeljenih bodova: {ukupni_bodovi}\n")

pattern = re.compile(r'\b\w{11,}\b')
for entry in finale_list:
    if pattern.search(entry["pjesma"]):
        print(f"Država {entry['drzava']} ima pjesmu s više od 10 slova: {entry['pjesma']}")

with open("eurovision_results.csv", "w", encoding="utf-8") as file:
    file.write("drzava,pjesma,izvodjac,bodovi")
    for entry in finale_list:
        file.write(f"{entry['drzava']},{entry['pjesma']},{entry['izvodjac']},{entry['bodovi']}")

print("Rezultati su zapisani u datoteku 'eurovision_results.csv'.")
