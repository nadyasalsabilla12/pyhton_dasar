# Polymorphism pada Method
class Kucing:
    def suara(self):
        return "Meow"

class Anjing:
    def suara(self):
        return "Guk guk"

hewan = [Kucing(), Anjing()]

for h in hewan:
    print(h.suara())

# Polymorphism dengan Inheritance
class Hewan:
    def suara(self):
        return "Hewan bersuara"

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

daftar_hewan = [Kucing(), Anjing(), Hewan()]

for h in daftar_hewan:
    print(h.suara())

# Polymorphism dengan Fungsi
def cetak_suara(hewan):
    print(hewan.suara())

cetak_suara(Kucing())
cetak_suara(Anjing())

# Polymorphism dengan Built-in Function
print(len("Python"))   
print(len([1, 2, 3]))  
print(len({"a": 1, "b": 2}))
