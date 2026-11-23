# List
buah = ["apel", "jeruk", "mangga"]

print(buah[0])   # apel

buah.append("pisang")

buah[1] = "anggur"

buah.remove("mangga")

print(buah)

# Tuple
warna = ("merah", "hijau", "biru")

print(warna[1])

for w in warna:
    print(w)

# Set 
angka = {1, 2, 3, 3, 4, 5}

print(angka)

angka.add(6)

angka.remove(2)

ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}

print(ganjil | genap)  
print(ganjil & genap)   
print(ganjil - genap)  
