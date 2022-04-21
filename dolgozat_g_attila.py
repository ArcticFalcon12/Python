# Írasd ki az összes sort
file1 = open('adatok.txt', 'r')
for i in range(6):
  print(f"Sor: {file1.readline()}")
# Olvasd be a fájl első sorát, amelyq megadja, hogy összesen hány adatsor van.    
file1.seek(0.0)
print(f"Sorok száma: {file1.readline()}")
# Írasd ki egy sorokszama.txt fájlbqa a sorok számát. 
file2 = open('sorokszama.txt', 'w')
file1.seek(0.0)
file2.write(file1.readline())
# Írasd ki külön az adatsorokat és külön az összes sorok számát.
file1.seek(0.0)
file1.readline()
for i in range(5):
    print("A sorok száma a 2. sortól:", file1.readline())
# a sorokban levő 3 szám szorzatát írd ki. Csak az adatsorokkal dolgozz!
file1.seek(0.0)
file1.readline()
sorok = []
for i in range(5):
    sorok = file1.readline().strip().split(";")
    szorzat = int(sorok[0]) * int(sorok[1]) * int(sorok[2])
    print("Szorzat:", szorzat)