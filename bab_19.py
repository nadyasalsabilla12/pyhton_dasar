from my_package import operasi, geometri

print(operasi.kurang(10, 4))     
print(geometri.luas_persegi(5))    

# Import fungsi tertentu dari package
from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print(kurang(20, 7))     
print(luas_persegi(8)) 

# Package di Python Standard Library
import os
import datetime

print(os.getcwd())        
print(datetime.date.today())   