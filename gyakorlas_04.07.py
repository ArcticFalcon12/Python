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
osszesEredmeny: list[Eredmeny] = []
#1. feladat ---------------------------------------------------------------------
file1.readline()
for sor in file1:
    egyEredmeny = Eredmeny(sor.strip())
    osszesEredmeny.append(egyEredmeny)
#2. feladat --------------------------------------------------------------------

noi_versenyzo = []
for egyAdat in osszesEredmeny:
    if egyAdat.Kategoria == "Noi" and egyAdat.TavSzazalek == 100:
        noi_versenyzo.append(egyAdat.Neve)
print(len(noi_versenyzo), "női versenyző teljesítette a teljes távot.")
#3. feladat ----------------------------------------------------------------

nevek = input("Adja meg egy versenyző nevét:")
benne_van = False
teljesitette = False
for egyAdat in osszesEredmeny:
    if nevek in egyAdat.Neve:
        benne_van = True
        if egyAdat.TavSzazalek == 100:
            teljesitette = True
if benne_van:
    print("Szerepel")
    if teljesitette:
        print("Teljesítette")
    else:
        print("Nem teljesítette")
else:
    print("Nem szerepel")
#4. feladat -----------------------------------------------------------------------
ido = osszesEredmeny[0].Idoeredmeny.split(":")
ido_osszeadva = ((int(ido[0]) * 3600) + (int(ido[1]) * 60) + int(ido[2]))
ido_elosztva = ido_osszeadva / 3600
ido_rendes = round(ido_elosztva,2)
print("Az első sportoló ideje átszámolva órába:", ido_rendes)
#5. feladat --------------------------------------------------------------------------
def ora_kiszamolo(ertek: str) -> float:
    ido = ertek.split(":")
    ora = ((int(ido[0]) * 3600) + (int(ido[1]) * 60) + int(ido[2])) / 3600
    return round(ora, 2)
print(ora_kiszamolo(osszesEredmeny[0].Idoeredmeny))
#for egyAdat in osszesEredmeny:
#    print("Sportoló neve:", egyAdat.Neve,";","Ideje:", ora_kiszamolo(egyAdat.Idoeredmeny))
    
#6. feladat ------------------------------------------------------------------
osszes_ora = 0
osszes_ferfi_versenyzo = 0
for egyAdat in osszesEredmeny:
    if egyAdat.Kategoria == "Ferfi" and egyAdat.TavSzazalek == 100:
        osszes_ferfi_versenyzo += 1
        osszes_ora += ora_kiszamolo(egyAdat.Idoeredmeny)
print("Az egész távot teljesítő férfi versenyzőknek az óra átlaga:", osszes_ora / osszes_ferfi_versenyzo)

#7. feladat ------------------------------------------------------------------
#Hány versenyző van akinél se az előtte lévő se az utána lévő nem ért célba de ő igen
darab = 0
for i in range(1,len(osszesEredmeny)-1):
    if osszesEredmeny[i].TavSzazalek == 100 and osszesEredmeny[i-1].TavSzazalek < 100 and osszesEredmeny[i+1].TavSzazalek < 100:
        darab += 1
print(darab,"darab ilyen versenyző van")