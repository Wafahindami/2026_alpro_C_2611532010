# Buat file dengan nama perulangan_for3_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2010 = int(input("Masukkan jumlah perulangan: "))

jumlah_2010 = 0
for i_2010 in range(1, ulang_2010 + 1):
    print(i_2010, end=" ")
    jumlah_2010 = jumlah_2010 + i_2010

    if i_2010 < ulang_2010:
        print("+", end=" ")
    else:
        print(" = ", jumlah_2010, end=" ")
print()
print("jumlah_2010 =", jumlah_2010)