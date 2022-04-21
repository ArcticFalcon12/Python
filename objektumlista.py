#Osztály létrehozás
class Nobeldijasok:
    ev : int
    nev: str
    szuletes_halalozas: str
    orszagkod: str

    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.ev = int(adatok[0])
        self.nev = adatok[1]
        self.szuletes_halalozas = adatok[2]
        self.orszagkod = adatok[3]
file1 = open('orvosi_nobeldijak.txt', 'r', encoding='utf-8')
#Üres objektum listalétrehozása: Ez egy olyan lista, ami sok NobelDijasok típusú objektumot tartalmaz
osszesNobelDijas: list[Nobeldijasok] = []


file1.readline()
for sor in file1:
    egyEmber = Nobeldijasok(sor.strip())
    osszesNobelDijas.append(egyEmber)
print(osszesNobelDijas[10].nev)
    
for egy in osszesNobelDijas:
    print(egy.ev)
for i in range(len(osszesNobelDijas)):
    print(osszesNobelDijas[i].nev)