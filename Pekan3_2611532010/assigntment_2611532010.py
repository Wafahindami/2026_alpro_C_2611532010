# Buat file dengan nama assigntment_2611532010.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2010 = int(input("Input angka-1: "))
angka2_2010 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2010)
print("Nilai awal angka2 =", angka2_2010)

# Assignment biasa
hasil = angka1_2010
print("\nOperator Assignment Biasa (=)")
print("hasil =", hasil)

# Assignment penambahan 
hasil = angka1_2010
hasil = angka2_2010
print("\nAssignment penambahan (+=)")
print ("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_2010
hasil = angka2_2010
print("\nAssignment pengurangan (-=)")
print("hasil =", hasil)

# Assignment perkalian
hasil = angka1_2010
hasil = angka2_2010
print("\nAssignment perkalian (*=)")
print("hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2010 != 0:
    hasil = angka1_2010
    hasil /= angka2_2010
    print("\nAssignment pembagian (/=)")
    print("hasil =", hasil)
    # Operator tambahan
    hasil = angka1_2010
    hasil //= angka2_2010
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_2010
    hasil %= angka2_2010
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("hasil =", hasil)

# Operator tambahan: assignment perpangkatan
hasil = angka1_2010
hasil **= angka2_2010
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)