# A Kutya osztály létrehozás
class Kutya:
    nev: str
    fajta: str
    szulIdo: str

    def __init__(self, neve: str, fajtaja: str, szulIdeje: int) -> None:
        self.nev = neve
        self.fajtaja = fajtaja
        self.szulIdo = szulIdeje
    def ugat(self): 
        print("Vau Vau...")

#Kutya osztájú objektumok létrehozása, azaz példányosítás -> 1 konkrét kutya
enKutyam = Kutya("Freya", "Németjuhász", 2020)
print("Kutyám neve:", enKutyam.nev)
print("Kora:", 2022 - enKutyam.szulIdo)
print("Fajtája:", enKutyam.fajtaja)

teKutyad = Kutya("Amogus", "kicsi kugyi", 1990)
print("Kutyád neve:", teKutyad.nev, ",","Kora:", 2022 - teKutyad.szulIdo, ",", "Fajtája:", teKutyad.fajtaja)

# A kutya osztály metódusának hívása
enKutyam.ugat()