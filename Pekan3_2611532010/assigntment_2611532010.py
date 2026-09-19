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
hasil_2010 = angka1_2010
print("\nOperator Assignment Biasa (=)")
print("hasil =", hasil_2010)

# Assignment penambahan 
hasil_2010 = angka1_2010
hasil_2010 = angka2_2010
print("\nAssignment penambahan (+=)")
print ("Hasil =", hasil_2010)

# Assignment pengurangan
hasil_2010 = angka1_2010
hasil_2010 = angka2_2010
print("\nAssignment pengurangan (-=)")
print("hasil =", hasil_2010)

# Assignment perkalian
hasil_2010 = angka1_2010
hasil_2010 = angka2_2010
print("\nAssignment perkalian (*=)")
print("hasil =", hasil_2010)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2010 != 0:
    hasil_2010 = angka1_2010
    hasil_2010 /= angka2_2010
    print("\nAssignment pembagian (/=)")
    print("hasil =", hasil_2010)
    # Operator tambahan
    hasil_2010 = angka1_2010
    hasil_2010 //= angka2_2010
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2010)
    hasil_2010 = angka1_2010
    hasil_2010 %= angka2_2010
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2010)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("hasil =", hasil_2010)

# Operator tambahan: assignment perpangkatan
hasil_2010 = angka1_2010
hasil_2010 **= angka2_2010
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2010)