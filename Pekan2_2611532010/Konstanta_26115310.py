# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14
print ("pi: %f" % (PI))
jari_2010 = float(input("masukkan nilai jari jari: "))
luas_2010 = PI * jari_2010 * jari_2010
print("Luas lingkaran dengan jari jari %.2f adalah %.2f" % (jari_2010, luas_2010))