# Contoh Inheritance Dasar
# Parent class
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan ini memiliki suara.")

class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} mengeong: Meow!")

class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

kucing = Kucing("Tom")
anjing = Anjing("Spike")

kucing.suara()
anjing.suara()

# Menambahkan Method Baru di Subclass
class Burung(Hewan):
    def suara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):
        print(f"{self.nama} sedang terbang!")
        
burung = Burung("Tyr")
burung.suara()
burung.terbang()

# Menggunakan super() unutk Akses Parent
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")

class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, jurusan, tahun_masuk):
        super().__init__(nama, jurusan)   # memanggil constructor parent
        self.tahun_masuk = tahun_masuk

    def info(self):
        super().info()  # memanggil method parent
        print(f"Tahun Masuk: {self.tahun_masuk}")

maba = MahasiswaBaru("Nadya", "Management", 2027)
maba.info()
