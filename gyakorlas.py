file1 = open('haromszogek.txt', 'r')
sorok = []
for sor in file1:
    sorok = sor.strip().split(" ")
    print(sorok)
file1.seek(0.0)
file1.readline()
print(file1.readline())
harmadik_sor = []
harmadik_sor = file1.readline().strip().split(" ")
print(harmadik_sor)

legnagyobb = max(harmadik_sor)
print(legnagyobb)
print(harmadik_sor[1])

file2 = open('ki.txt', 'w')
file2.write(harmadik_sor[1])

file1.seek(0.0)
for i in range(4):
    sorok = file1.readline()
    print(sorok)