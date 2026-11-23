# Membuat function sederhana
def sapa():
    print("Halo, selamat datang di Python!")

sapa()

# Function dengan paramenter
def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Nadya")
sapa_nama("Fathir")

# Function dengan return value 
def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)

# Default paramenter
def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Caca")
sapa_orang()        

# Function dengan banyak argumen (*args dan *kwargs)
# *args
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)


# **kwargs
def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Nadya", umur=16, kota="Bnadung")

