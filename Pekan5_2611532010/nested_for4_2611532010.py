# Buat file dengan nama nested_for4_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2010 = int(input("masukkan tinggi pola (bilangan genap, misal 10):"))

if tinggi_2010 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2010 = tinggi_2010 
    c_2010 = a_2010
    lebar_2010 = (2 * tinggi_2010)- 2

    for i_2010 in range(1, tinggi_2010 +1):
        b_2010 = c_2010 + 1

        for j_2010 in range (1, lebar_2010 + 1):

            # Baris atas dan bawah
            if i_2010 == 1 or i_2010 == tinggi_2010:
                if j_2010 == 1 or j_2010 == lebar_2010:
                    print("#", end="")
                else:
                    print("=", end="")

                # Baris isi
            else:
                if j_2010 == 1 or j_2010 == lebar_2010:
                    print("|", end="")
                else:
                    if j_2010 == c_2010:
                        print("<", end="")
                    elif j_2010 == b_2010:
                        print(">", end="")
                    elif j_2010 == (lebar_2010 - c_2010):
                        print("<", end="")
                    elif j_2010 == (lebar_2010 - c_2010 + 1):
                        print(">", end="")
                    elif j_2010 > b_2010 and j_2010 < (lebar_2010 - c_2010):
                        print(".", end="")
                    else:
                        print(" ", end="")
        
        print()

        # logika asli java
        a_2010 -= 2

        if a_2010 <= 0:
            c_2010 = (-a_2010) + 2
        else:
            c_2010 = a_2010