# Buat file dengan nama if_elif_else1_nim.py
# Buat program untuk kodisional if
# Nama variabel ditambah 4 digit terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2010 = int(input("Input Umur Anda = "))
sim_2010 = input("Apakah Anda Sudah Punya SIM (y/t): ")[0]

if umur_2010 >= 17 and sim_2010 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_2010 >= 17 and sim_2010 != "y":
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2010 < 17 and sim_2010 == "y":
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
print("Program Selesai") 