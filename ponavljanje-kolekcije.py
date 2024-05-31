import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

def generiraj_satnicu():
    return round(random.uniform(4, 6), 2)

radnici = []
for _ in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = generiraj_satnicu()
    radnik = {
        "ime": ime,
        "prezime": prezime,
        "satnica": satnica
    }
    radnici.append(radnik)

for radnik in radnici:
    radnik["tjedni_sati"] = random.randint(20, 30)

isplate = []
for radnik in radnici:
    ime = radnik["ime"]
    prezime = radnik["prezime"]
    satnica = radnik["satnica"]
    tjedni_sati = radnik["tjedni_sati"]
    isplata = round(satnica * tjedni_sati, 2)
    isplate.append((ime, prezime, isplata))

for ime, prezime, isplata in isplate:
    print(f"{ime} {prezime}: Isplata - {isplata}")

ukupna_isplata = sum(isplata for _, _, isplata in isplate)
print(f"Ukupna isplata za ovaj tjedan: {ukupna_isplata}")


prosjecna_isplata = ukupna_isplata / len(isplate)
print(f"Prosječna isplata za ovaj tjedan: {prosjecna_isplata}")


print("Radnici s isplatom iznad prosjeka:")
for ime, prezime, isplata in isplate:
    if isplata > prosjecna_isplata:
        print(f"{ime} {prezime}")
