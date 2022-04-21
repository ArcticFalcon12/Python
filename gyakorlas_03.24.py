#Létrehozom az autó osztály
class Auto:
    marka: str
    evjarat: int
    szin: str
    hengerurtartalom: int

    def __init__(self, markaja: str, evjarata: int, szine: str, hengerurtartalma: int) -> None:
        self.marka = markaja
        self.evjarat = evjarata
        self.szin = szine
        self.hengerurtartalom = hengerurtartalma
    def kocsihang(self):
        print("Vrum Vrum..")
#Autó osztályú objektumok létrehozása
enAutom = Auto("Audi", 2022, "Fekete", 100000000000000000000000)
print("Autóm márkája:", enAutom.marka, ",","Évjárata:", enAutom.evjarat, ",","Színe:", enAutom.szin, ",","Hengerűrtartalma:", enAutom.hengerurtartalom)
enAutom.kocsihang()