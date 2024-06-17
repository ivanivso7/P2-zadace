"""
Podatke iz datoteke rezultati.csv učitati kao listu ntorki oblika
(ime, prezime, bodovi).
Iterirati kroz sve studente i ispisati samo one koji su položili ispit
(br. bodova veci od 49)
"""
from csv import reader

csv_file_path = r'C:\Users\Korisnik\Desktop\Fakultet\Programiranje 2\zadaće\P1_23_24_1K_REZ.csv'

with open(csv_file_path, 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    studenti = list(map(tuple, csv_reader))

studenti = [student for student in studenti if len(student) >= 3 and student[2].isdigit()]

studenti.sort(key=lambda student: student[1])

ocjene_po_rangu = {
    'Nedovoljan': 0,
    'Dovoljan': 0,
    'Dobar': 0,
    'Vrlodobar': 0,
    'Odličan': 0
}

for student in studenti:
    bodovi = int(student[2])
    if bodovi < 50:
        ocjene_po_rangu['Nedovoljan'] += 1
    elif 50 <= bodovi < 65:
        ocjene_po_rangu['Dovoljan'] += 1
    elif 65 <= bodovi < 80:
        ocjene_po_rangu['Dobar'] += 1
    elif 80 <= bodovi < 90:
        ocjene_po_rangu['Vrlodobar'] += 1
    elif 90 <= bodovi <= 100:
        ocjene_po_rangu['Odličan'] += 1

print("Sortirana lista studenata prema prezimenima:")
for student in studenti:
    print(f"{student[1]}, {student[0]}: {student[2]} bodova")

print("\nBroj ostvarenih ocjena po bodovnom rangu:")
for rang, broj in ocjene_po_rangu.items():
    print(f"{rang}: {broj}")

