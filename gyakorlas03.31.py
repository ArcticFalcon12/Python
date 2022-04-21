#Osztály létrehozása
class Eredmeny:
    Neve: str
    Rajtszam: int
    Kategoria: str
    Idoeredmeny: str
    TavSzazalek: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.Neve = adatok[0]
        self.Rajtszam = int(adatok[1])
        self.Kategoria = adatok[2]
        self.Idoeredmeny = adatok[3]
        self.TavSzazalek = int(adatok[4])
file1 = open('ub2017egyeni.txt', 'r')
file1.readline()
for sor in file1:
    #Egyadat nevű Eredmeny típusú objektum létrehozása
    egyAdat = Eredmeny(sor)
    print("Neve:", egyAdat.Neve, ";", "Ideje:", egyAdat.Idoeredmeny, "")
file1.seek(0.0)
file1.readline()
darab = 0
#Hány női versenyző van
for sor in file1:
    egyAdat = Eredmeny(sor)
    if egyAdat.Kategoria == "Noi":
        darab += 1
print("A női versenyzők száma:", darab)
file1.seek(0.0)
file1.readline()
szazalek = []
for sor in file1:
    egyAdat = Eredmeny(sor)
    szazalek.append(int(egyAdat.TavSzazalek))
print("A leghamarabb befejezett versenyző százaléka:", min(szazalek))