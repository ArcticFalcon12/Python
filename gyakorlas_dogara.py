class Helyjegy:
    ules: int	
    tol: int
    ig: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(" ")
        self.ules = int(adatok[0])
        self.tol = int(adatok[1])
        self.ig = int(adatok[2])
        
file1 = open("eladott.txt", "r")
osszesEredmeny: list[Helyjegy] = []
file1.readline()
for sor in file1:
    egyEredmeny = Helyjegy(sor.strip())
    osszesEredmeny.append(egyEredmeny)
osszes_utazas = len(osszesEredmeny)
print(osszes_utazas)