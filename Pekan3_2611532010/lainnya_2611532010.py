# Buat file dengan nama lainnya_NiM.py
# Nama variabel ditambah 4 digit Nim terakhir contoh: angka_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2010  = nilai_dicari in data
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in", data, "=", hasil_2010)

# Operator not in
hasil_2010 = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data, "=", hasil_2010)


print("\n========================================")
print("2. OPERATOR IDENTITAS")
print("========================================")

# objek1 menggunakan list dari input pengguna
objek1_2010 = data

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2010 = objek1_2010

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2010 = data.copy()

print("objek1 =", objek1_2010)
print("objek2 =", objek2_2010)
print("objek3 =", objek3_2010)

# Operator is
hasil = objek1_2010 is objek2_2010
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil)

# Operator is not
hasil = objek1_2010 is not objek3_2010
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_2010 is objek3_2010)
print("objek1 == objek3 =", objek1_2010 == objek3_2010)