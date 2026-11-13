xarajatlar = {}
try:
    fayl = open("xarajatlar.txt", "r")
    for qator in fayl:
        qismlar = qator.strip().split(": ")
        xarajatlar[qismlar[0]] = int(qismlar[1])
    fayl.close()
except FileNotFoundError:
    pass

while True:
    nom = input("Xarajat nomi (stop - tugatish): ")
    if nom == "stop":
        break
    summa = int(input("Summa: "))
    xarajatlar[nom] = summa

fayl = open("xarajatlar.txt", "w")

jami = 0
for nom in xarajatlar:
    print(f"{nom}: {xarajatlar[nom]}")
    fayl.write(f"{nom}: {xarajatlar[nom]}\n")
    jami = jami + xarajatlar[nom]
fayl.close()
print("Jami:", jami)