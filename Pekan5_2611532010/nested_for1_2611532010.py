# Buat file dengan nama nested_for1_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2010 = int(input("masukkan nilai batas:  "))
for line in range(1, batas_2010 + 1):
    for j_2010 in range(1, (-1 * line + batas_2010 + 1)):
        print(".", end="")
    print(line)