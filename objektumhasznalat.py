# OSZTÁLY:

class Haromszog:
    a: int
    b: int
    c: int
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])    
        
    # osztály metódusa: szöveggel visszatérve megmondja, hogy a számok háromszöget alkotnak-e    
    def haromszoge(self) -> str:
        if self.a<self.b+self.c and self.b<self.a+self.c and self.c<self.a+self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."
    
    # osztály metódusa: egész számként visszaadja a háromszög kerületét
    def kerulet(self)-> int            :
        return self.a + self.b + self.c
    def derekszogu(self) -> bool:
        return self.a^2 + self.b^2 == self.c^2
    def szerepel_E(self, szam: int) -> bool:
        if szam == self.a or szam == self.b or szam == self.c:
            return True
        else:
            return False
    
file1 = open('haromszog.txt', 'r')
lista = []
file1.readline()
for sor in file1:
    lista.append(sor.strip().split("*"))
print(lista)

for item in lista:
    print(item)
    egyHaromszog = Haromszog(item)
    print(egyHaromszog.haromszoge())
    print(egyHaromszog.kerulet()) 
 
    
    
    
print("--------------------------------------------------------------------------") 
print("05.25 feladatok")
#Kérj be a felhasznlótól 3 számot ( megfelelő adatszerkezetben),
# majd írd neki, hogy háromszöget alkotnak-e
lista_haromszog = []
haromszog_a = (input("Adja meg a háromszög a oldalát:"))
haromszog_b = (input("Adja meg a háromszög a oldalát:"))
haromszog_c = (input("Adja meg a háromszög a oldalát:"))
lista_haromszog.append(haromszog_a)
lista_haromszog.append(haromszog_b)
lista_haromszog.append(haromszog_c)
teljesHaromszog = Haromszog(lista_haromszog)
print(teljesHaromszog.haromszoge())
#A háromszög derékszögű e
print(teljesHaromszog.derekszogu())
#Szerepel-e benne egy paraméterként megadott szám
bekert_szam = int(input("Adjon meg egy számot:"))
print(teljesHaromszog.szerepel_E(bekert_szam))