def glavna_funkcija():
    putanja_datoteke = r"C:\Users\Korisnik\Desktop\Fakultet\Programiranje 2\zadaće\P1_23_24_1K_REZ.csv"
    
    podaci_o_studentima = ucitaj_podatke_o_studentima(putanja_datoteke)
    
    if podaci_o_studentima:
        
        polozeni_studenti = [student for student in podaci_o_studentima if student[2] > 49]
        polozeni_studenti.sort(key=lambda x: x[1])  
        print("Studenti koji su položili ispit i sortirani po prezimenima:")
        for student in polozeni_studenti:
            print(f"{student[0]} {student[1]} - Bodovi: {student[2]}")
    else:
        print("Nema podataka o studentima ili nisu pronađeni podaci o položenim ispitima.")

def ucitaj_podatke_o_studentima(putanja_datoteke):
    podaci_o_studentima = []
    try:
        with open(putanja_datoteke, 'r', encoding='utf-8') as datoteka:
            linije = datoteka.readlines()
            for linija in linije[1:]:
                podaci = linija.strip().split(',')
                ime = podaci[0]
                prezime = podaci[1]
                try:
                    bodovi = int(podaci[2])
                except (ValueError, IndexError):
                    bodovi = 0  
                podaci_o_studentima.append((ime, prezime, bodovi))
    except FileNotFoundError:
        print(f"Datoteka '{putanja_datoteke}' nije pronađena.")
    
    return podaci_o_studentima

if __name__ == "__main__":
    glavna_funkcija()
