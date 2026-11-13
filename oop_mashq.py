# class Talaba:
#     def __init__(self,ism,yosh):
#         self.ism = ism
#         self.yosh = yosh
#     def tanishtir(self):
#         print(f"Men {self.ism}, yoshim {self.yosh}")

# t1 = Talaba("Ali", 20)
# t2 = Talaba("Vali", 21)

# t1.tanishtir()
# t2.tanishtir()





class Talaba:
    def __init__(self, ism, yosh, baho):
        self.ism = ism
        self.yosh = yosh
        self.baho = baho
    def tanishtir(self):
        print(f"Men {self.ism}, yoshim {self.yosh}, bahoyim {self.baho}")

    def a_alomi(self):
        if self.baho >=4:
            return "A'lo/yaxshi"
        return "Yaxshilanishi kerak"

    def yosh_oshir(self):
        self.yosh = self.yosh + 1


    def baho_ozgartir(self, yangi_baho):
        self.baho = yangi_baho
        
talabalar = [
    Talaba("Ali", 20, 10),
    Talaba("Vali", 21, 3),
    Talaba("Sher", 22, 4),
]

for t in talabalar:
    t.tanishtir()
    print(t.a_alomi())

jami = 0
for t in talabalar:
    jami = jami + t.baho
print("O'rtacha:", jami / len(talabalar))

# t1.yosh_oshir()
# t1.tanishtir()
# print(t1.a_alomi())
# t2.yosh_oshir()

# print(t2.a_alomi())          # baho 3: Yaxshilanishi kerak
# yangi = int(input("Yangi baho: "))
# t2.baho_ozgartir(yangi)
# print(t2.a_alomi())  
