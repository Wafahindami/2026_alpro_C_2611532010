# buat file dengan nama aritmatika_2611532010.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2010 = int(input("Input angka-1: "))
angka2_2010 = int(input("Input angka-2: "))

# Penjumlahan
hasil = angka1_2010 + angka2_2010
print("/nOperator Penjumlahan")
print("hasil =" , hasil)

# Pengurangan
hasil = angka1_2010 - angka2_2010
print("/nOperator Pengurangan")
print("hasil =" , hasil)

# Perkalian
hasil = angka1_2010 * angka2_2010
print("/nOperator Perkalian")
print("hasil =" , hasil)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2010 != 0:
    hasil = angka1_2010 / angka2_2010
    print("/nOperator Pembagian")
    print("hasil =" , hasil)

    hasil = angka1_2010 // angka2_2010
    print("/nOperator Pembagian bulat")
    print("hasil =" , hasil)

    hasil = angka1_2010 % angka2_2010
    print("/nOperator Sisa bagi")
    print("hasil =" , hasil)
else:
    print("angka kedua tidak boleh bernilai 0,")

# Pangkat
hasil = angka1_2010 ** angka2_2010
print("/nOperator Pangkat")
print("hasil =" , hasil)