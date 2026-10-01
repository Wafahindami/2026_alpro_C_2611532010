# Buat file dengan nama perulangan_for2_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2010 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_2010-1)
for i_2010 in range(ulang_2010):
    print(i_2010, end=" ")
print()
print("perulangan ke-1 sampai ke-", ulang_2010)
for i_2010 in range(1, ulang_2010+1):
    print(i_2010, end=" ")