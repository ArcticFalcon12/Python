#Osztály létrehozása
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
file1.readline()
for sor in file1:
    #Irassuk ki csak a nevüket
    egyEmber = Nobeldijasok(sor)
    print("Neve:", egyEmber.nev)
    
    
file1.seek(0.0)
file1.readline()
osszesen = 0
for sor in file1:
    #Hány Nobel Díjas van?
    osszesen += 1
    egyNobel = Nobeldijasok(sor)
print("Összesen ennyi Nobel Díjas van:", int(osszesen))


file1.seek(0.0)
file1.readline()
darab = 0
for sor in file1:
    #Hány magyar Nobel Díjas van?
    egyMagyar = Nobeldijasok(sor.strip())
    if egyMagyar.orszagkod == "H":
        darab = darab + 1
print("Összesen ennyi Magyar Nobel Díjas van:", darab)


file1.seek(0.0)
file1.readline()
evek = []
for sor in file1:
    #Mikor kapták meg az első Nobel Díjat
    elsoNobel = Nobeldijasok(sor)
    evek.append(elsoNobel.ev)
print("Az első Nobel Díjat ekkor kapták:", min(evek))


file1.seek(0.0)
file1.readline()
szerepel = False
for sor in file1:
    #Szerepel e a listában Archibald nevű ember
    elsoNev = Nobeldijasok(sor)
    if "Otto" in elsoNev.nev:
        szerepel = True
if (szerepel):
    print("A Nobel Díjasok között szerepel Otto nevű ember")
else:
    print("A Nobel Díjasok között nem szerepel Otto nevű ember")
    

file1.seek(0.0)
file1.readline()
szuletesek = []
for sor in file1:
    #Írasd ki soronként, hogy hány éves korában halt meg a díjazott
    mikorHalt = Nobeldijasok(sor)
    szuletesek = mikorHalt.szuletes_halalozas.strip().split("-")
    if szuletesek[1] != "":
        kor = int(szuletesek[1]) - int(szuletesek[0])
        print("Neve", mikorHalt.nev, ";", "Életkora:", kor)