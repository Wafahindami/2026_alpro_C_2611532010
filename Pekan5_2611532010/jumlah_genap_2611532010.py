# Buat file dengan nama jumlah_genap_nim.py
# Buat program untuk menghitung jumlah bilangan genap
# Nama variabel ditambah 4 digit terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2010 = int(input("masukkan nilai batas: "))

jumlah_genap_2010 = 0
for i_2010 in range(1, ulang_2010 + 1):
    if i_2010 % 2 == 0:
        print(i_2010, end=" ")
        jumlah_genap_2010 += i_2010

        if i_2010 < ulang_2010:
            print("+", end=" ")
        else:
            print(" = ", jumlah_genap_2010, end="")
print()
print("jumlah =", jumlah_genap_2010)