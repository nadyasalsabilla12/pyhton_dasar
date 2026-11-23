# Membuat module
# matematika.py
def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b

# Menggunakan Module
# main.py
import matematika

print(matematika.tambah(2, 3)) 
print(matematika.kali(4, 5))     

# Import dengan Alias
import matematika as m

print(m.tambah(10, 5))  

# Import Fungsi Tertentu
from matematika import tambah

print(tambah(7, 3)) 

# Built-in Modules
import math

print(math.sqrt(16)) 
print(math.pi)         

