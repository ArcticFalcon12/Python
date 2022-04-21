class Focimeccs:
    Fordulo: int
    Hazai_gol: int
    Vendeg_gol: int
    Hazai_felido_gol: int
    Vendeg_felido_gol: int
    hazai_csapat: str
    vendeg_csapat: str
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(" ")
        self.Fordulo = int(adatok[0])
        self.Hazai_gol = int(adatok[1])
        self.Vendeg_gol = int(adatok[2])
        self.Hazai_felido_gol = int(adatok[3])
        self.Vendeg_felido_gol = int(adatok[4])
        self.hazai_csapat = adatok[5]
        self.vendeg_csapat = adatok[6]
file1 = open('meccs.txt', 'r')
osszesEredmeny: list[Focimeccs] = []
file1.readline()
for sor in file1:
    egyEredmeny = Focimeccs(sor.strip())
    osszesEredmeny.append(egyEredmeny)
#0. Feladat ---------------------------------------------------------------------------
osszes_meccs = len(osszesEredmeny)
print("Összesen", osszes_meccs, "mérkőzés van")
#1. Feladat ---------------------------------------------------------------------------
#Kérje be egy forduló számát majd annak az adatait írja ki
bekert_szam = int(input("Adja meg egy forduló számát (1-20):"))
for egyAdat in osszesEredmeny:
    if bekert_szam == egyAdat.Fordulo:
        print(egyAdat.hazai_csapat,"-", egyAdat.vendeg_csapat,":", egyAdat.Hazai_gol,"-",egyAdat.Vendeg_gol," (",egyAdat.Hazai_felido_gol,"-",egyAdat.Vendeg_felido_gol,")", sep='')
