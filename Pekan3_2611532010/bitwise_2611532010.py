# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1:_1234
# Program ini menggunakan fungsi input()

print("\n========================================")
print("3. OPERATOR BITWISE")
print("========================================")

angka1_2010 = int(input("Masukkan angka bitwise-1: ")) 
angka2_2010= int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_2010 =", angka1_2010, "| biner =", bin(angka1_2010))
print("angka2_2010 =", angka2_2010, "| biner =", bin(angka2_2010))

# Bitwise AND
hasil = angka1_2010 & angka2_2010
print("\nBitwise AND (&)")
print(angka1_2010, "&", angka2_2010, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1_2010 | angka2_2010
print("\nBitwise OR (|)")
print(angka1_2010, "|", angka2_2010, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1_2010 ^ angka2_2010
print("\nBitwise XOR (^)")
print(angka1_2010, "^", angka2_2010, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1_2010
print("\nBitwise NOT (~)")
print("~", angka1_2010, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_2010 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_2010, "<<", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1_2010 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_2010, ">>", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))