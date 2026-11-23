# Membuat dictionary
mahasiswa = {
    "nama": "Nadya",
    "umur": 16,
    "jurusan": "Informatika"
}

print(mahasiswa)

# Membuat data
print(mahasiswa["nama"])  
print(mahasiswa.get("umur")) 

# Menambah dan mengubah data
mahasiswa["angkatan"] = 2023   
mahasiswa["umur"] = 16       

print(mahasiswa)

# Menghapus data
mahasiswa.pop("jurusan")
del mahasiswa["nama"]      

print(mahasiswa)

# Iterasi dictionary
for key, value in mahasiswa.items():
    print(key, ":", value)

# Nested dictionary
kampus = {
    "mahasiswa1": {"nama": "Nadya", "umur": 16},
    "mahasiswa2": {"nama": "Fathir", "umur": 15}
}

print(kampus["mahasiswa1"]["nama"])
