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
print("------------- 1. Feladat ------------------")
bekert_szam = int(input("Adja meg egy forduló számát (1-20):"))
for egyAdat in osszesEredmeny:
    if bekert_szam == egyAdat.Fordulo:
        print(egyAdat.hazai_csapat,"-", egyAdat.vendeg_csapat,":", egyAdat.Hazai_gol,"-",egyAdat.Vendeg_gol," (",egyAdat.Hazai_felido_gol,"-",egyAdat.Vendeg_felido_gol,")", sep='')
#2. Feladat ---------------------------------------------------------------------------
print("------------- 2. Feladat ----------------")
bekert_csapat = input("Adjon meg egy csapat nevet:")
bekert_csapat_szerepelt = False
for egyAdat in osszesEredmeny:
    if bekert_csapat == egyAdat.hazai_csapat or bekert_csapat == egyAdat.vendeg_csapat:
        bekert_csapat_szerepelt = True
if bekert_csapat_szerepelt:
    print("Szerepelt")
else:
    print("Nem szerepelt")

#3. Feladat -------------------------------------------------
print("------------------ 3. Feladat -------------------")
gol = 0
for egyAdat in osszesEredmeny:
    if egyAdat.vendeg_csapat == "Nyulak":
       gol += egyAdat.Vendeg_gol
print(gol)

#4. Feladat --------------------------------------------------
def forditottake(a: int, b: int, c: int, d: int) -> bool:
    return ( c > d and b > a) or (d > c and a > b)
for egyAdat in osszesEredmeny:
    forditottake(egyAdat.Hazai_gol, egyAdat.Hazai_felido_gol, egyAdat.Vendeg_gol, egyAdat.Vendeg_felido_gol)
    