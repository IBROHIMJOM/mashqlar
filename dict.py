narx = {"olma": 5000, "non": 3000}
# print(narx["olma"])
# narx["sut"] = 8000
# print(narx)


nom = input("Mahsulot: ")
if nom in narx:
    print(narx[nom])
else:
    print("topilmadi")