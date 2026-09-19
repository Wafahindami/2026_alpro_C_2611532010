# Buat file dengan nama perbandingan_2611532010.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2010 = int(input("Input angka-1: "))
angka2_2010 = int(input("Input angka-2: "))

# Lebih besar dari 
hasil = angka1_2010 > angka2_2010
print("\nOperator Lebih besar dari")
print("angka1 > angka2 =", hasil)

# Lebih kecil dari
hasil = angka1_2010 < angka2_2010
print("\nOperator Lebih kecil dari")
print("angka1 < angka2 =", hasil)

# lebih besar dari atau sama dengan
hasil = angka1_2010 >= angka2_2010
print("\nOperator Lebih besar dari atau sama dengan")
print("angka1 >= angka2 =", hasil)

# lebih kecil dari atau sama dengan
hasil = angka1_2010 <= angka2_2010
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =", hasil)

# sama dengan
hasil = angka1_2010 == angka2_2010
print("\nOperator sama dengan")
print("angka1 == angka2 =", hasil)

# tidak sama dengan
hasil = angka1_2010 != angka2_2010
print("\nOperator tidak sama dengan")
print("angka1 != angka2 =", hasil)

# Tambahan: perbandingan berantai dalam python
hasil = 0 < angka1_2010 < 100
print("\nPerbandingan berantai")
print("0 < angka1 < 100 =", hasil)

hasil = 0 < angka2_2010 < 100
print("0 < angka2 < 100 =", hasil)