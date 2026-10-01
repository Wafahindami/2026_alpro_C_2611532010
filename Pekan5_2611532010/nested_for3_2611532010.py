# Buat file dengan nama nested_for3_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2010 = int(input("masukkan nilai batas:"))
for i_2010 in range(batas_2010+1):
    for j_2010 in range(batas_2010+1):
        print (i_2010+j_2010, end=" ")
    print() # pindah ke baris berikutnya